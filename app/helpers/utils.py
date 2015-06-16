#!/usr/bin/env python3.4
#encoding: UTF-8
#

'''
utils.py

'''

import string
import random
from tornado import gen


import requests

@gen.coroutine
def http_get(url, cookies):
    r = requests.get(url, cookies=cookies)
    return r.text


def mock():
    pass


