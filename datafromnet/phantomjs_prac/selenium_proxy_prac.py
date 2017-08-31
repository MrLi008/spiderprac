# coding=utf8
from selenium import webdriver
service_args = [
    '--proxy=localhost:55312',
    '--proxy-type=socks'
]
phantomjsroot = 'F:\\software\\developertools\\phantomjs\\phantomjs-2.1.1-windows\\bin'

driver = webdriver.PhantomJS(phantomjsroot+'\\phantomjs.exe')
driver.get('http://icanhazip.com')
print (driver.page_source)
driver.close()