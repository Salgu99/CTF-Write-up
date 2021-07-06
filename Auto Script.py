from selenium import webdriver
from time import sleep

url = 'https://webhacking.kr/old.php'

#no error log
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(executable_path='chromedriver', options=options)


id = 'kimsalgu'
pw = 'salgu531'
passch = ''



##### Login ####
driver.get(url='https://webhacking.kr/login.php')
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/form/table/tbody/tr[1]/td[2]/input').send_keys(id)
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/form/table/tbody/tr[2]/td[2]/input').send_keys(pw)
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/form/input').click()
cookie = driver.get_cookie('PHPSESSID')
driver.get(url=url)


# old 01
import old01 as o1
o1.getflag(cookie)
driver.refresh()

# old 02
import old02 as o2
o2.getFlag(cookie)
driver.refresh()

#old 03
#USE HEADER

#old 04


#old 05
import old05 as o5
o5.getflag(cookie)
driver.refresh()


#old 06
import old06 as o6
o6.getflag(cookie)
driver.refresh()

#old 07


sleep(30)