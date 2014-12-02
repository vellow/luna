#!/usr/bin/env python
#encoding: UTF-8

'''
Baidu UUAP Login

'''

import urllib2
import cookielib
import urllib
import requests

class Login:
    def __init__(self):
        # CAS Server Address
        self.url = "http://itebeta.baidu.com:8100/login"
        # Create Global Cookie Handler
        cookie = cookielib.CookieJar()
        cookieProc = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(cookieProc)
        urllib2.install_opener(opener)
        self.step_1()

    def step_1(self):
        # Read login form
        lurl = "http://itebeta.baidu.com:8100/login"
        getUuap = urllib2.urlopen(lurl)
        htmlGet = getUuap.read()
        # Get the magic param 'lt'
        htmlString = str(htmlGet)
        start = htmlString.index("<input type=\"hidden\" name=\"lt\" value=\"")
        end = htmlString.index("\"", start+38)
        lt = htmlString[start+38:end]
        params = {"_rememberMe": "on", "username" : "zhanzhixiang", "password" : "zhanzhixiang", "rememberMe" : "true", "lt" : lt, "execution" : "e1s1", "_eventId" : "submit", "type" : "1"}
        urlParams = urllib.urlencode(params)
        req = urllib2.Request(lurl, urlParams)
        htmlPost = urllib2.urlopen(req)
        # print htmlPost.read()
        self.step_2()

    def step_2(self):
        params = {"excution": "e1s2", "_eventId": "submit", "setCookiePathFailure": "[http://setCookie1.com, http://setcookie2.com]"}
        urlParams = urllib.urlencode(params)
        req = urllib2.Request(self.url, urlParams)
        htmlPost = urllib2.urlopen(req)
        # print htmlPost.read()
        # get_todo()
        url = "http://m1-art-devapp3.vm.baidu.com:8766/oa/user/getTodo.do"
        # req = urllib2.Request(url)
        res = requests.get(url)
        print res.json()

# def get_todo():

if __name__=='__main__':
    Login()



