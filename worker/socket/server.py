#!/usr/bin/env python
#encoding: UTF-8

import zerorpc
import logging
from auth_service.cas.auth import Login
from data_service.api_service import Data
# from _common.utils import *

logging.basicConfig()

class Services:
    def __init__(self):
        pass

    def auth_itebeta(self, username):
        data = Login().login_cas_itebeta(username)
        return data

    def auth_uuap(self, username, password):
        data = Login().login_cas_uuap(username, password)
        return data

    def get_data(self, url, cookies):
        data = Data().get_data(url, cookies)
        return data


s = zerorpc.Server(Services())
s.bind("tcp://0.0.0.0:4242")
s.run()
