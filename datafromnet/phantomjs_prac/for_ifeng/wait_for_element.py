# coding=utf8
from selenium.webdriver.support import ui
import time
import codecs


def visiable(driver, condition):

    wait = ui.WebDriverWait(driver, 25)

    count = 0
    while True:
        try:
            elem = driver.find_elements_by_tag_name(condition)
            with codecs.open('temp/ifeng_auto'+str(count)+'.html', 'wb', 'utf-8') as f:
                f.write(driver.page_source)
            count += 1
        except Exception as e:
            print e
            elem = None
        # print elem
        if elem not in (None, [] ):
            break
        time.sleep(0.1)

    return elem

def get_all_a(driver, url, limitformat=''):
    driver.get(url)

    elems = visiable(driver, 'a')

    hrees = []
    for elem in elems:
        href = elem.get_attribute('href')
        # print href,
        if href not in (None, '') and limitformat in href:
            # print '--------ye', href
            hrees.append(href)
    return hrees

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
            with codecs.open('temp/')