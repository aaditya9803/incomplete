from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = "C:\\Users\\aadit\\Desktop\\temp\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.com/SSK-Aluminum-Tool-Free-Enclosure-Portable/dp/B0892BK5L6/?_encoding=UTF8&pd_rd_w=cji46&content-id=amzn1.sym.6e9da02f-f7a3-444f-aea6-9ef09ed8bb89&pf_rd_p=6e9da02f-f7a3-444f-aea6-9ef09ed8bb89&pf_rd_r=T3FVHC205PZCXCTXARGC&pd_rd_wg=JM8an&pd_rd_r=9e2c74a3-d2d5-4712-838c-5239c394a98a&ref_=pd_gw_ci_mcx_mr_hp_d&th=1")
abc = driver.find_element(By.ID, "productTitle")
print(abc.text)
driver.quit()