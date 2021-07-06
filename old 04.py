import hashlib
import threading

from selenium import webdriver

rainbow = {}

def getflag(cookie=None):
    t = threading.Thread(target=rain)
    t.start()
    t.join()

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path='chromedriver', options=options)

    driver.get(url='https://webhacking.kr/challenge/web-04/')
    driver.delete_all_cookies()
    driver.add_cookie(cookie)
    driver.refresh()

    while True:
        valEL = driver.find_elements_by_xpath('/html/body/center/form/table/tbody/tr[1]/td/b')
        for val in valEL:
            val = valEL
        try:
            result = rainbow[val]
            print('==================')
            print('RESULT IS '+result)
            print('==================')

            driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[2]/td[2]/input').send_keys(result)
            driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[2]/td[3]/input').click()
            try:
                al = driver.switch_to_alert()
                if 'already solved' in al.text:
                    print('#04 PASS ')
                al.accept()
            except:
                print("ERROR NO.04")
            finally:
                driver.close()
            break
        except:
            driver.refresh()



def rain():
    for i in range(10000000,10500000):
        key = str(i)+'salt_for_you'
        tmp = key
        for j in range(0, 500):
            key = hashlib.sha1(key.encode()).hexdigest()
        rainbow['%s'%(key)] = tmp

if __name__ == '__main__':

    #rain()
    coo = {'name':'PHPSESSID', 'value':'e8j3vm6uvuh4fqlgml274or3ek'}
    getflag(coo)
