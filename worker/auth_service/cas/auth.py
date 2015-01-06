#!/usr/bin/env python
#encoding: UTF-8

'''
CAS Login

'''

import requests

class Login:
    def __init__(self):
        # CAS Server Address
        self.cas_itebeta_url = "http://itebeta.baidu.com:8100/login"
        self.cas_uuap_url = "http://uuap.baidu.com/login"
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'baidu.com',
            'Referer': 'http://www.baidu.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'
        }
        self.cookies = dict()

    def login_cas_itebeta(self, username, service):
        self.login_url = self.cas_itebeta_url + '?service=' + service
        # Read login form
        r = requests.get(self.login_url)
        r.encoding = 'UTF-8'
        self.cookies.update(r.cookies)
        # Get the magic param 'lt'
        htmlString = r.text
        start = htmlString.index("<input type=\"hidden\" name=\"lt\" value=\"")
        end = htmlString.index("\"", start+38)
        lt = htmlString[start+38:end]
        params = {"_rememberMe": "on", "username" : username, "password" : username, "rememberMe" : "true", "lt" : lt, "execution" : "e1s1", "_eventId" : "submit", "type" : "1"}
        r = requests.post(self.login_url, data=params, cookies=self.cookies)
        r.encoding = "UTF-8"
        self.cookies.update(r.cookies)
        return self.login_app()

    def login_cas_uuap(self, username, password, service):
        self.login_url = self.cas_itebeta_url + '?' + service
        # Read login form
        r = requests.get(self.login_url)
        r.encoding = 'UTF-8'
        self.cookies.update(r.cookies)
        # Get the magic param 'lt'
        htmlString = r.text
        start = htmlString.index("<input type=\"hidden\" name=\"lt\" value=\"")
        end = htmlString.index("\"", start+38)
        lt = htmlString[start+38:end]
        params = {"_rememberMe": "on", "username" : username, "password" : password, "rememberMe" : "true", "lt" : lt, "execution" : "e1s1", "_eventId" : "submit", "type" : "1"}
        r = requests.post(self.login_url, data=params, cookies=self.cookies)
        r.encoding = "UTF-8"
        self.cookies.update(r.cookies)
        return self.login_app()

    def login_app(self):
        params2 = {"excution": "e2s2", "_eventId": "submit", "setCookiePathFailure": "http://setCookie1.com", "setCookiePathFailure": "http://setcookie2.com"}
        r2 = requests.post(self.login_url, data=params2, cookies=self.cookies, allow_redirects=False)
        self.app_url = r2.headers.get('location')
        return self.get_app_ticket()

    def get_app_ticket(self):
        r3 = requests.get(self.app_url, cookies=self.cookies, allow_redirects=False)
        self.cookies.update(r3.cookies)
        return self.cookies


if __name__=='__main__':
    ins = Login()
    print ins.login_to_cas()
