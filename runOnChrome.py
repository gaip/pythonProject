from selenium import webdriver
import time
from selenium.webdriver.chrome.options import  Options

options = Options()
options.headless = True

print("testStart")
driver = webdriver.Chrome(options=options,executable_path="C:\\Users\\Eleme\\PycharmProjects\\pythonProject\\venv\\drivers\\chromedriver.exe")

driver.get("http://5elementslearning.dev/demosite")

print("testStart")
print(driver.find_element_by_link_text("My Account").text)
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_name("email_address").clear()
driver.find_element_by_name("email_address").send_keys("abc@demo.com")
print(driver.find_element_by_name("email_address").get_attribute("value"))

print(driver.find_element_by_name("email_address").tag_name)
print(driver.find_element_by_name("email_address").is_displayed())
print(driver.find_element_by_name("email_address").text)

driver.find_element_by_name("password").send_keys("ml1610_0")

driver.find_element_by_xpath("//x:button[@id='tdb5']/x:span[2]").click()


print("testEnd")
time.sleep(3)
driver.quit()