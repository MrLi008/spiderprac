# coding=utf8
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import sys

# sys.path.join('')

driver = webdriver.Chrome()
driver.get('http://pythonscraping.com')
links = driver.find_elements_by_tag_name('a')

for link in links:
    if not link.is_displayed():
        print 'this link: ', link.get_attribute('href') , ' is a trap'


fields = driver.find_elements_by_tag_name('input')
for field in fields:
    if not field.is_displayed():
        print 'do not change the value of ', field.get_attribute('name'), ' .....'