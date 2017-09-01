# coding=utf8
from selenium.webdriver.support import ui
import time
import codecs
import random

def visiable(driver, condition):


    # count = 0
    while True:
        try:
            elems = driver.find_elements_by_tag_name(condition)
            time.sleep(2)
            # with codecs.open('temp/ifeng_auto'+str(random.randint(0,100000000))+'.html', 'wb', 'utf-8') as f:
            #     f.write(driver.page_source)
            # count += 1
        except Exception as e:
            print e
            elems = None
        # print elem
        if elems not in (None, [] ):
            break

    links = []
    for elem in elems:
        try:
            links .append(elem.get_attribute('href'))
        except Exception as e:
            print e

    return links

def get_all_a(driver, url, limitformat='',links=set(), depth=0, maxdepth=1):
    # if url in links:
    #     return
    if depth > maxdepth:
        return
    print 'urls: ', len(links), 'request: ', url
    driver.get(url)

    hrees = visiable(driver, 'a')

    for href in hrees:

        if href not in (None, '') and limitformat in href:
            # print '--------ye', href
            if href in links:
                continue
            with open('temp/links_forum.txt', 'wb+') as f:
                f.write(href)
                f.write('\n')
            links.add(href)
            get_all_a(driver, href, limitformat=limitformat,links=links,depth=depth+1,maxdepth=maxdepth)

    return links

def get_all_forum(driver, url):
    return get_all_a(driver, url, 'http://bbs.auto.ifeng.com/forum-')


def get_all_thread(driver, url):
    return get_all_a(driver, url, 'http://bbs.auto.ifeng.com/thread-')


def get_all_thread_page(driver, url, limitform=''):
    # all forum:
    forums = get_all_forum(driver, url)

    for forum in forums:
        threadlinks = get_all_thread(driver, forum)

        for threadlink in threadlinks:
            driver.get(threadlink)
            elems = visiable(driver, 'a')
            # with codecs.open('temp/')