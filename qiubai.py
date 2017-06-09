import urllib.request
import re

url = 'https://www.qiushibaike.com/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
headers = {'User-Agent':user_agent}
try:
    request = urllib.request.Request(url,headers=headers)
    respone = urllib.request.urlopen(request)

    #print(respone.read())

    content = respone.read().decode('utf-8')
    pattern = re.compile('<div.*?author clearfix">.*?'+
                         '<a.*?<img.*?>.*?'+
                         '</a>.*?'+
                         '<div.*?'+
                         'content">.*?'+
                         '<span>(.*?)</span>.*?'+
                         '</div>.*?'+
                         '<div class="stats.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern, content)
    print(len(items),'my')
    for item in items:
        print(item,'a')

except urllib.request.URLError or e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)