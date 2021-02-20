from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options



driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://5elementslearning.dev/demosite')
print(driver.find_element_by_link_text("My Account").text)
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_name("email_address").clear()
driver.find_element_by_name("email_address").send_keys("gaip@gaip.de")
print(driver.find_element_by_name("email_address").get_attribute("value"))

print(driver.find_element_by_name("email_address").tag_name)
print(driver.find_element_by_name("email_address").is_displayed())
print(driver.find_element_by_name("email_address").text)

driver.find_element_by_name("password").send_keys("ml1610_0")

driver.find_element_by_id('tdb5').click()

driver.find_element_by_link_text('Log Off').click()

driver.find_element_by_link_text('Continue').click()

driver.find_element_by_link_text("My Account").click()

driver.find_element_by_partial_link_text("Account").click()
print(driver.find_element_by_name("email_address").is_displayed())
print(driver.find_element_by_xpath("//input[@name='password']").is_displayed())
print(driver.find_element_by_css_selector("#tdb5").is_enabled())
driver.find_element_by_name("keywords").send_keys("unreal")
driver.find_element_by_xpath("//input[contains(@title,'Quick Find')]").click()
time.sleep(2)

print(driver.find_element_by_class_name("productListingHeader").is_displayed())
driver.quit()

driver.quit()