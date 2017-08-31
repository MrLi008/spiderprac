# coding=utf8
from selenium import webdriver
from selenium.webdriver import Chrome
import requests
import time

phantomjsroot = 'F:\\software\\developertools\\phantomjs\\phantomjs-2.1.1-windows\\bin'

# driver = webdriver.Chrome()
driver = webdriver.PhantomJS(phantomjsroot+'\\phantomjs.exe')

url = 'https://mp.weixin.qq.com/s/gnx44150Ck61hJZnBp3lOA'
driver.get(url)

begin = time.time()


def replace_all(url):
    return url.replace('/','_').replace(':','_').replace('.','_').replace('?','_')

# print url.replace('/','_')
for img in driver.find_elements_by_tag_name('img'):
    imgurl = img.get_attribute('data-src')
    try:
        imgdata = requests.get(imgurl)
    except Exception as e:
        print e, 'in ....'
        continue
    with open('temp/img/'+replace_all(imgurl)+'.jpg', 'wb') as f:
        f.write(imgdata.content)



end = time.time()
print 'time: ', end-begin
# driver.get_screenshot_as_file('temp/'+url.replace('/','_').replace(':','_')+'.png')
# driver.close()