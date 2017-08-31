# coding=utf8


import wait_for_element
from selenium import webdriver
from selenium.webdriver import Chrome, PhantomJS
import requests
import codecs

phantomjsroot = 'F:\\software\\developertools\\phantomjs\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'



# driver = Chrome()
driver = PhantomJS(phantomjsroot)

url = 'http://bbs.auto.ifeng.com'




# url = 'http://bbs.auto.ifeng.com/thread-2938733-1-1.html'


links = wait_for_element.get_all_forum(driver, url)
with codecs.open('temp/links-forum.txt', 'wb', 'utf-8') as f:
    for link in links:
        f.write(link+'\n')

    f.write('\n')

