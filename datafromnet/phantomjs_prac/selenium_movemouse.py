# coding=utf8
from selenium import webdriver
from selenium.webdriver import Chrome, PhantomJS


from selenium.webdriver import ActionChains
import unittest
import time
phantomjsroot = 'F:\\software\\developertools\\phantomjs\\phantomjs-2.1.1-windows\\bin'
class AdditionTest(unittest.TestCase):
    additiondriv = None
    def setUp(self):
        global additiondriv
        # additiondriv = webdriver.Chrome()
        additiondriv = webdriver.PhantomJS(phantomjsroot+'\\phantomjs.exe')
        # url = 'http://pythonscraping.com/pages/javascript/draggableDemo.html'
        # url = 'http://sahitest.com/demo/dragDropMooTools.htm'

        url = 'https://mp.weixin.qq.com/s/gnx44150Ck61hJZnBp3lOA'
        additiondriv.get(url)
        print 'time start'
        time.sleep(1)
        print 'time endding'


    def tearDown(self):
        print ('tearing down the test')
        global additiondriv
        time.sleep(3)
        additiondriv.close()




    def test_drag(self):

        global additiondriv
        element = additiondriv.find_element_by_id('dragger')
        targets = additiondriv.find_elements_by_class_name('item')
        print element
        print targets

        # actions.drag_and_drop(element, target)
        for target in targets:
            actions = ActionChains(additiondriv)
            # actions.move_to_element(element)
            actions.click_and_hold(element)
            actions.move_to_element(target)
            actions.release(element)
            time.sleep(2)
            actions.perform()




if __name__ == '__main__':
    unittest.main()