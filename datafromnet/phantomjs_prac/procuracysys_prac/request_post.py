# coding=utf8
import requests
from selenium import webdriver
from selenium .webdriver import Chrome
import time
import json
import traceback

def getlogon():

    driver = Chrome()

    driver.get('http://127.0.0.1:8080')
    input_phone = driver.find_element_by_css_selector('input[name="phone"]')
    input_phone.send_keys('admin')
    input_pswd = driver.find_element_by_css_selector('input[name="password"]')
    input_pswd.send_keys('admin')
    submitbutton = driver.find_elements_by_class_name('btn-login')[0]
    submitbutton.click()
    time.sleep(2)


    return driver

def postdatato(url, driver=Chrome()):
    try:
        data = {
            "investigateLegalCase":{
                "id":1,
                "investigate_subtype":"test_investigate_subtype2",
                "investigate_content":"test_investigate_content2",
                "investigate_score":1,
                "investigate_submit_time":1504075719000,
                "investigate_type":"test_investigate_type2",
            },

            "id": 1,
            "investigate_subtype": "test_investigate_subtype2",
            "investigate_content": "test_investigate_content2",
            "investigate_score": 1,
            "investigate_submit_time": 1504075719000,
            "investigate_type": "test_investigate_type2",
        }
        # postresult = requests.post(url, data=data)
        cookies = driver.get_cookies()
        headers = {
            'Content-Language':'zh-CN',
            'Content-Type':'application/json;charset=ISO-8859-1'
            # 'Content-Type':'application/x-www-form-urlencoded'
        }
        # print 'cookies: ', cookies

        # postresult = requests.post(url, data=data, cookies=cookies,headers=headers)
        # url = 'http://127.0.0.1:8080/infomanage.html'
        postresult = requests.post(url, cookies=cookies,headers=headers,data=data)
        print postresult, type(postresult.text), len(postresult.text)
        result = json.loads(postresult.text, encoding='utf-8')
        print result.get('data', None)

    except Exception as e:
        traceback.print_exc()
        # return None这个是测试用例

    # return postresult


def t_url_apis_investigatelegalcase_addone():
    urls = [
        'http://127.0.0.1:8080//apis/investigatelegalcase/list',
        'http://127.0.0.1:8080//apis/investigatelegalcase/addOne',
        'http://127.0.0.1:8080//apis/investigatelegalcase/filterby_investigate_type',
        'http://127.0.0.1:8080//apis/investigatelegalcase/updateOne',
        'http://127.0.0.1:8080//apis/investigatelegalcase/deleteOne',
    ]

    driver = getlogon()
    for url in urls:
        postdatato(url, driver)

        # print postdata
    driver.close()


if __name__ == '__main__':
    t_url_apis_investigatelegalcase_addone()