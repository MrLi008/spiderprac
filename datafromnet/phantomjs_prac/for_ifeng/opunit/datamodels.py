# coding=utf8
'''存放需要保存的数据'''

import threading
import traceback
from funcs import  visiable, filterlinksbypattern,phantomjsroot
from staticvariable import filters
from selenium import webdriver

class HrefSet:
    def __init__(self,**kwargs):
        self.kwargs = dict()
        # init kwargs
        self.kwargs['driver'] = webdriver.PhantomJS(phantomjsroot)
        self.kwargs['url'] = kwargs.get('url')
        self.kwargs['hrefset'] = self


        self.hrefset = set()
        self.hreflist = []
        self.MAXTOP = 4000
        self.top = 0
        self.pop = -1

        self.lock = threading._allocate_lock()



    def getnext(self):
        self.lock.acquire()

        self.pop += 1

        result = None

        if self.pop < self.top and self.top < self.MAXTOP:
            result = self.hreflist[self.pop]

        print 'in href set, getnext: ', self.pop, self.hreflist[self.pop]

        self.lock.release()

        return result


    def add(self, href):

        self.lock.acquire()


        if self.top >= self.MAXTOP:
            return
        if isinstance(href, list):

            for h in href:
                if h not in self.hrefset:
                    self.hrefset.add(h)
                    self.hreflist.append(h)

                    self.top += 1
                    print 'in href set, add', self.top
        else:
            if href not in self.hrefset:
                self.hrefset.add(href)
                self.hreflist.append(href)

                self.top += 1
                print 'in href set, add'

        self.lock.release()

    def func(self, url='', driver=webdriver.PhantomJS(phantomjsroot)):

        driver.get(url)
        links = visiable(driver)
        links = filterlinksbypattern(links, filters)
        self.add(links)
        print self.pop, self.top, len(links)




'''控制访问链接的线程数, 并保持稳定

    :func 无参
'''
class ControlThread:
    def __init__(self, hrefset=HrefSet()):

        self.threadnumbser = 10
        self.hrefset = hrefset

    def process(self, driver):
        nextdata = self.hrefset.getnext()
        if nextdata == None:
            return False

        self.hrefset.func(url=nextdata,driver=driver)
        return True

    def function_(self, i, driver):
        while self.process(driver):
            print 'for ', str(i)

    def run(self):
        threadlist = []

        for i in range(self.threadnumbser):
            driver = webdriver.PhantomJS(phantomjsroot)
            t = threading.Thread(target=self.function_,
                               args=(i, driver))

            threadlist.append(t)
            t.start()

        for t in threadlist:
            t.join()