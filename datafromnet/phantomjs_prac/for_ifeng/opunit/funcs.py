# coding=utf8
import time
from selenium.webdriver import Chrome, PhantomJS
from staticvariable import phantomjsroot, weburl
import re

class MaxLengthSubString:
    def __init__(self):
        self.substring = ''



# 获取最长子串
'''
    usage:
        substring = MaxLengthSubString()
        getMaxLengthSubStringBetween(0,0,str1, str2, 0,0,0, substring)
    :result
        substring.substring
'''
def getMaxLengthSubStringBetween(index1, index2, str1, str2,
                                 samelength, strbegin=0, strend=0,
                                 maxlength=MaxLengthSubString()):
    print index1, index2,str1, str2, strbegin, strend, samelength, maxlength.substring
    if index1 >= len(str1) or index2 >= len(str2):
        return samelength

    if strend-strbegin == samelength and len(maxlength.substring) < samelength:
        maxlength.substring = str1[strbegin:strend]

    if str1[index1] == str2[index2]:
        samelength += 1
        index1 += 1
        index2 += 1
        return getMaxLengthSubStringBetween(index1, index2, str1, str2, samelength,
                                            index1-samelength, index1, maxlength)
    else:

        return max(
            samelength,
            getMaxLengthSubStringBetween(index1+1, index2, str1, str2, 0,
                                         min(index1+1, index2+1), min(index1+1,index2+1), maxlength),
            getMaxLengthSubStringBetween(index1, index2+1, str1, str2, 0,
                                         min(index1,index2+1), min(index1,index2+1), maxlength),
        )


def test_getMaxLengthSubStringBetween():
    str1 = '12345667777'
    str2 = '12345664777'

    substring = MaxLengthSubString()

    print getMaxLengthSubStringBetween(0,0,str1, str2, 0, 0, 0, substring)
    print substring.substring
















# 等待页面加载完成


def visiable(driver, tagname='a', attrname='href'):


    count = 0
    while True:
        try:
            elems = driver.find_elements_by_tag_name(tagname)
            time.sleep(2)
            # with codecs.open('temp/ifeng_auto'+str(random.randint(0,100000000))+'.html', 'wb', 'utf-8') as f:
            #     f.write(driver.page_source)

        except Exception as e:
            print e
            elems = None
        # print elem
        count += 1
        if count > 10:
            break
        if elems not in (None, [] ):
            break

    if elems in (None, []):
        return []
    # 由于driver get url 获取了其他的url后, 原来的数据会被清除
    # 这里单独将tag attr value 保存
    links = []
    for elem in elems:
        try:
            href = elem.get_attribute(attrname)
            if href in (None, ''):
                continue
            links .append(href)
        except Exception as e:
            print e
    print 'links: ', type(links), len(links)
    return links

def test_visiable():
    driver = Chrome()
    url = weburl
    driver.get(url)

    links = visiable(driver, 'a')
    for link in links:
        print 'link: ', link







# 过滤连接列表
def filterlinksbypattern(links, filters):
    if not isinstance(links, list):
        return []
    result = []
    if isinstance(filters, list):
        for filter_ in filters:
            cmp = re.compile(filter_)

            for link in links:
                # print link
                if len(link) <= len(filter_):
                    continue
                res = cmp.findall(link)
                if res not in (None, []):
                    result.append(link)

    else:
        cmp = re.compile(filters)
        for link in links:
            res = cmp.findall(link)
            if res not in (None, []):
                for r in res:
                    result.append(r)



    return result

def test_filterlinksbyparttern():
    links = [
        'http://bbs.auto.ifeng.com/forum-1020337-2.html',
        'http://bbs.auto.ifeng.com/forum-1020254-89.html',
        'http://bbs.auto.ifeng.com/forum-1020747-1.html',
        'http://bbs.auto.ifeng.com/forum-1020214-4.html',
        'https://id.ifeng.com/user/register?backurl=http://bbs.auto.ifeng.com/forum-1020358-1.html',
        'http://bbs.auto.ifeng.com/forum-1020556-1.html',
        'http://bbs.auto.ifeng.com/forum-1020234-80.html',
        'http://bbs.auto.ifeng.com/forum-1020375-9.html',
        'http://bbs.auto.ifeng.com/forum-1020201-2.html',
        'http://bbs.auto.ifeng.com/forum-1020236-9.html',
        'http://bbs.auto.ifeng.com/forum-1020716-9.html',
        'http://bbs.auto.ifeng.com/forum-1020246-1.html',
        'http://bbs.auto.ifeng.com/forum-1020783-7.html',
        'http://bbs.auto.ifeng.com/forum-1020718-7.html',
        'http://bbs.auto.ifeng.com/forum-1020238-7.html',
    ]
    filters = 'http://bbs.auto.ifeng.com/forum-10202'
    result = filterlinksbypattern(links, filters)
    for res in result:
        print 'res: ', res























def main():
    # test_getMaxLengthSubStringBetween()
    test_visiable()
    test_filterlinksbyparttern()



if __name__ == '__main__':
    main()