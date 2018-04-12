import logging
import hdtHttp as http
import win

host = "192.168.69.134"

url = "http://" + host + "/cgi-bin/luci"
data = {"luci_username": "root", "luci_password": ""}


headers = {'Content-Type' : 'application/x-www-form-urlencoded'}

LOG_FORMAT="%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s "
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

main_win = win.hdg3200_win()
main_win.show_win()

req = http.HttpReq(host)
req.gatewaydetect()
req.test_start()


'''
try:
    f = requests.post(url, data, timeout=1, allow_redirects=False)
    print(f.url)
    print(f.status_code)
    print(f.cookies.get('sysauth'))
    print(f.headers['Location'])

    cookie = f.cookies.get('sysauth')

    furl= "http://" + host  + f.headers['Location']
    print(furl)
    f = requests.get(furl, timeout=5, allow_redirects=False, cookies={'sysauth': cookie})
    # print(f.text)


    purl=furl + "/admin/factory/module_check/pingcheck"
    print(purl)
    p = requests.get(purl, timeout=1, allow_redirects=False, cookies={'sysauth': cookie})
    print(p.text)
except requests.exceptions.Timeout:
    print("connection timeout")

'''
