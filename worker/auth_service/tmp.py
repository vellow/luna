import urllib2
import cookielib
import urllib
import requests

headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'baidu.com',
            'Referer': 'http://www.baidu.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'
        }

lurl = "http://itebeta.baidu.com:8100/login"
cookie = cookielib.CookieJar()
cookieProc = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookieProc)
urllib2.install_opener(opener)

r = requests.get(lurl)
r.encoding = 'UTF-8'
# Get the magic param 'lt'
htmlString = r.text
start = htmlString.index("<input type=\"hidden\" name=\"lt\" value=\"")
end = htmlString.index("\"", start+38)
lt = htmlString[start+38:end]
params = {"_rememberMe": "on", "username" : "zhanzhixiang", "password" : "zhanzhixiang", "rememberMe" : "true", "lt" : lt, "execution" : "e1s1", "_eventId" : "submit", "type" : "1"}

service = 'http://m1-art-devapp3.vm.baidu.com:8766/oa/'
loginUrl = 'http://itebeta.baidu.com:8100/login.jsp'

r = requests.post(lurl, data=params, headers=headers)