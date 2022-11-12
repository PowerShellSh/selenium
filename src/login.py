from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep
LOGIN_ID = 'syusyu0125'
PASS = 'Riku-Sena.0820'
driver = webdriver.Chrome(executable_path=r"../chromedriver")

url = "https://www.sbisec.co.jp/ETGate/WPLETmgR001Control?OutSide=on&getFlg=on&burl=search_home&cat1=home&cat2=tool&dir=tool&file=home_opappli_03.html"
driver.get(url)

loginID = driver.find_element(By.XPATH, "/html/body/div[@id='middleArea']/div[@id='middleAreaM']/table[@class='loTblMid']/tbody/tr/td[@class='loSide']/div[@id='side']/div[@id='new_login']/form[@class='margin-4']/dl/dd[1]/div[@id='user_input']/input")
loginPass = driver.find_element(By.XPATH,"/html/body/div[@id='middleArea']/div[@id='middleAreaM']/table[@class='loTblMid']/tbody/tr/td[@class='loSide']/div[@id='side']/div[@id='new_login']/form[@class='margin-4']/dl/dd[2]/div[@id='password_input']/input")

loginID.send_keys(LOGIN_ID)
loginPass.send_keys(PASS)

btn = driver.find_element(By.XPATH,"/html/body/div[@id='middleArea']/div[@id='middleAreaM']/table[@class='loTblMid']/tbody/tr/td[@class='loSide']/div[@id='side']/div[@id='new_login']/form[@class='margin-4']/p[@class='sb-position-c']/input")

sleep(3)

btn.click()
