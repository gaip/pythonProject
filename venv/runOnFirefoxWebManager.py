from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import  Options

options = Options()
options.headless=True

driver = webdriver.Firefox(ChromeDriverManager().install())

driver.get('http://5elementslearning.dev/demosite')
time.sleep(3)
browser.quit()