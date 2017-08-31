# coding=utf8

from selenium import webdriver
from selenium.webdriver import Chrome, PhantomJS
from static_variable import phantomjsroot
from bs4 import BeautifulSoup
import time
import codecs

url = 'http://bbs.auto.ifeng.com'

driver = webdriver.Chrome()
def replace_all(url):
    return url.replace('/','_').replace(':','_').replace('.','_').replace('?','_')


def getHrefFromPage(bsobj):
    return bsobj.find_elements_by_tag_name('a')

def getBSObjFrom(url):


    driver.get(url)
    html = driver.page_source
    with codecs.open(replace_all(url)+'.html', 'wb', 'utf-8') as f:
        f.write(html)
    bsobj = BeautifulSoup(html, 'html.parser')
    return bsobj


def t(url, urlset=set()):
    print 'request: ', url
    if url in urlset:
        return

    urlset.add(url)
    try:
        bsobj = getBSObjFrom(url)

    except Exception as e:
        print e
        return

    urls = getHrefFromPage(bsobj)

    for url in urls:
        t(url)


if __name__ == '__main__':
    urlset = set()
    testurl = url

    t(testurl, urlset)