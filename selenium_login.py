from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_driver = "C:\\Users\\aadit\\Desktop\\chromedriver.exe"
driver = webdriver.Chrome(executable_path = chrome_driver)
driver.get(url="https://secure-retreat-92358.herokuapp.com/")
f_name = driver.find_element(By.XPATH, "/html/body/form/input[1]")
time.sleep(10)
f_name.send_keys("atriox")
l_name = driver.find_element(By.XPATH, "/html/body/form/input[2]")
time.sleep(10)
l_name.send_keys("neu")
mail = driver.find_element(By.XPATH, "/html/body/form/input[3]")
time.sleep(10)
mail.send_keys("donisfirst2@gmail.com")
mail.send_keys(Keys.ENTER)
time.sleep(10)

driver.quit()
