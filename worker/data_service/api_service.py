#!/usr/bin/env python
#encoding: UTF-8

'''
Data Service

'''

import requests
import json

class Data:
    def __init__(self):
        pass

    def get_data(self, url, cookies):
        r = requests.get(url, cookies=cookies)
        return r.text
