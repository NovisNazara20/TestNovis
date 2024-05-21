from selenium import webdriver
from time import sleep
#
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
#
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(executable_path='C:/driverfirefox/geckodriver.exe')
sleep(3)
driver.get("https://www.demoblaze.com/")
sleep(2)

 # waktu
waktu = WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath('//*[@id="signin2"]'))
waktu.click()
sleep(2) 

# # # Username Daftar
# sleep(2)
userDaftar = WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath('//*[@id="sign-username"]'))
sleep(2)
userDaftar.send_keys("saya")
sleep(1)

# # # Password Daftar
# sleep(2)
passDaftar = WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath('//*[@id="sign-password"]'))
sleep(2)
passDaftar.send_keys("saya123")
sleep(1)

# # KLIK BUTTON daftar
daftar = WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath('//*[@id="signInModal"]/div/div/div[3]/button[2]'))
daftar.click()
sleep(2)


# //*[@id="cartur"]
# //*[@id="tbodyid"]/div[1]/div/div/h4/a
# //*[@id="tbodyid"]/div[2]/div/a