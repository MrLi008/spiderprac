# coding=utf8
'''存放需要保存的数据'''

import threading
import traceback
from funcs import  visiable, filterlinksbypattern,phantomjsroot
from staticvariable import filters
import codecs
from selenium import webdriver

class HrefSet:
    def __init__(self):


        self.hrefset = set()
        self.hreflist = []
        self.MAXTOP = 1000
        self.top = 0
        self.pop = -1

        self.lock = threading._allocate_lock()



    def getnext(self):
        self.lock.acquire()

        result = None
        self.pop += 1


        if self.pop < self.top:
            result = self.hreflist[self.pop]

            print 'in href set, getnext: ',self.top, self.pop, self.hreflist[self.pop]

        self.lock.release()

        return result


    def add(self, href):

        self.lock.acquire()


        if self.top <= self.MAXTOP:
            if isinstance(href, list):

                for h in href:
                    if h not in self.hrefset:
                        self.hrefset.add(h)
                        self.hreflist.append(h)

                        self.top += 1
            else:
                if href not in self.hrefset:
                    self.hrefset.add(href)
                    self.hreflist.append(href)

                    self.top += 1

        print 'in href set, add', self.top, self.pop

        self.lock.release()

    def func(self, url='', driver=webdriver.PhantomJS(phantomjsroot)):

        driver.get(url)
        links = visiable(driver)
        links = filterlinksbypattern(links, filters)
        self.add(links)

        # 获取论坛主题
        thread_substring = 'thread_subject'
        try:
            subject = driver.find_element_by_id(thread_substring)
            with codecs.open('temp/subject.txt', 'ab+', encoding='utf-8') as f:
                f.write(subject.text+'\t'+url+'\n')
            print subject.text
        except Exception  as e:
            print ' no this id'


        print '-'*100, self.pop, self.top, len(links)




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
        print 'next data: ', nextdata
        self.hrefset.func(url=nextdata,driver=driver)
        return True

    def function_(self, i, driver):
        while self.process(driver):
            print 'for ', str(i)

    def run(self):
        threadlist = []
        drivers = []
        for i in range(self.threadnumbser):
            driver = webdriver.PhantomJS(phantomjsroot)
            drivers.append(driver)

        for i in range(self.threadnumbser):
            t = threading.Thread(target=self.function_,
                               args=(i, drivers[i]))

            threadlist.append(t)

            t.start()

        print 'finish init'
        for t in threadlist:

            t.join()
            print 'finish....', t