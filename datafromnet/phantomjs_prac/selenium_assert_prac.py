# coding=utf8
from selenium import webdriver


driver = webdriver.Chrome()
#
driver.get('http://en.wikipedia.org/wiki/Monty_Python')
print driver.title
assert 'Monty Python' not in driver.title
driver.close()


# with webdriver.Chrome() as driver:
#     driver.get('http://en.wikipedia.org/wiki/Monty_Python')
#     assert 'Monty Python' not in driver.title