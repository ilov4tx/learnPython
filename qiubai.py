import urllib.request
import re

url = 'https://www.qiushibaike.com/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
headers = {'User-Agent':user_agent}
try:
    request = urllib.request.Request(url,headers=headers)
    respone = urllib.request.urlopen(request)
    print(respone.read())

except urllib.request.URLError or e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)

content = urllib.request.respone.read().decode('utf-8')
pattern = re.compile()

