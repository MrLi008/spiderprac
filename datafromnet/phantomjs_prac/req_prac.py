# coding=utf8
import requests
from bs4 import BeautifulSoup
import selenium

myses = requests.session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',

}
url = 'https://www.whatismybrowser.com/'
req = myses.get( url, headers=headers)
print req
print req.cookies
print req.headers

bsobj = BeautifulSoup(req.text, 'html.parser')

print (bsobj.find('div', {'class':'string-major'}).get_text())
with open('web.html', 'w') as f:
    f.write(req.text)

