#!/usr/bin/env python
#encoding: UTF-8

'''
Data Service

'''

import requests
import json
# from .._common import utils

class Data:
    def __init__(self):
        pass

    def get_data(self, url, cookies):
        r = requests.get(url, cookies=cookies)
        r.encoding = "UTF-8"
        # data = json.loads(r.text)
        return r.text
