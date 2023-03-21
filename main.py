# import requests
print('new')
from selenium import webdriver

options = webdriver.ChromeOptions()
# options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("https://www.rockhursths.edu/")

search_bar = driver.find_element_by_id('site-search-box')
search_bar.send_keys("Test")
