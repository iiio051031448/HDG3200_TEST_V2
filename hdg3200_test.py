import logging
import win
import instance_lock as i_lock
import atexit
import hdt_logger



one_lock = None

#hdt_logger.debug("test start")
#logging.FileHandler("system.log")
#log_format = "%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s "
#logging.basicConfig(level=logging.DEBUG, format=log_format, filename="system.log", filemode="w")
hdt_logger.HDLogger.logger.debug("=======")

def exit_cleanup():
    hdt_logger.HDLogger.logger.error("=======exit_cleanup========")
    if one_lock:
        one_lock.unlock()

atexit.register(exit_cleanup)

one_lock = i_lock.OneInstanceLock()

main_win = win.hdg3200_win()
if not one_lock.is_locked():
    main_win.show_win()
else:
    main_win.show_one_instance_warning_box()

hdt_logger.HDLogger.logger.debug("--------------- EXITTING ---------------")

one_lock.unlock()

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
