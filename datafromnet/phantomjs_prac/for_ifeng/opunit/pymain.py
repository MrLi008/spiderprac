# coding=utf8

from selenium import webdriver
from selenium.webdriver import Chrome, PhantomJS
from datamodels import ControlThread, HrefSet
import traceback
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

    url = 'http://bbs.auto.ifeng.com'

    # driver = Chrome()
    driver = PhantomJS(phantomjsroot)

    hrefset = HrefSet(url=url)
    print hrefset

    driver.get(url)
    links = visiable(driver)
    print len(links)
    links_ = filterlinksbypattern(links, filters)

    print len(links_)
    hrefset.add(links_)

    ct = ControlThread(hrefset=hrefset)
    ct.run()
