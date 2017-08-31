# coding=utf8
import requests
import codecs


# url = 'http://bbs.auto.ifeng.com/forum.php'
url = 'http://bbs.auto.ifeng.com/api/index.htm'
html = requests.get(url)

with codecs.open('temp/req_forum.html', 'wb', 'utf-8') as f:
    f.write(html.content)


