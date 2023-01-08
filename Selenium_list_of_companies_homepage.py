from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Users\\aadit\\Desktop\\temp\\chromedriver.exe")
driver.get("http://nepalstock.com/")
# data = driver.find_element(By.XPATH, '//*[@id="nepse-stats"]/div[3]/div[2]/table[1]/tbody/tr[1]/td[2]')
data = driver.find_elements(By.CSS_SELECTOR, "#top-gainers tbody tr td b")
for datas in data:
    print(datas.text)
driver.quit()
