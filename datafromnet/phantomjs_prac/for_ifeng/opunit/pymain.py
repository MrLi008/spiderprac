# coding=utf8

from selenium import webdriver
from selenium.webdriver import Chrome, PhantomJS
from datamodels import ControlThread, HrefSet
import traceback
import threading
from staticvariable import phantomjsroot, filters

from funcs import visiable, filterlinksbypattern





# def func_(**kwargs):
#     try:
#         driver = kwargs.get('driver')
#         url = kwargs.get('url')
#         hrefset = kwargs.get('hrefset')
#
#     except Exception as e:
#         traceback.print_exc()
#         return
#     driver.get(url)
#     links = visiable(driver)
#     links = filterlinksbypattern(links, filters)
#     hrefset.add(links)
#     print hrefset.pop, hrefset.top



if __name__ == '__main__':

    # url = 'http://bbs.auto.ifeng.com'
    url = 'http://bbs.auto.ifeng.com/forum-1020774-1.html'

    # driver = Chrome()
    driver = PhantomJS(phantomjsroot)

    hrefset = HrefSet()
    print hrefset

    driver.get(url)
    links = visiable(driver)
    print len(links)
    links_ = filterlinksbypattern(links, filters)

    print len(links_)
    hrefset.add(links_)

    ct = ControlThread(hrefset=hrefset)
    t = threading.Thread(target=ct.run)
    t.start()
    t.join()
