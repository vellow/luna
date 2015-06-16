#!/usr/bin/env python3.4
#encoding: UTF-8
#

'''
generator handlers

'''

from app.models import lines
from app.handlers.base import XHRHandler
from app.helpers import utils

from tornado import gen
import uuid

from app.helpers import cas

authCache = {}

class MockHandler(XHRHandler):

    def initialize(self):
        self.login = cas.Login()

    @gen.coroutine
    def get(self):
        try:
            user = self.get_query_argument('user')
        except:
            user = None

        url = self.get_query_argument('service')
        isMock = self.get_query_argument('isMock')
        userid = self.get_cookie('LUNA-UUID')
        auth = authCache.get(userid)

        if userid==None or auth==None or user:
            auth = self.login.login_cas_itebeta(user, url)

            userid = str(uuid.uuid1())
            authCache[userid] = auth
            self.set_cookie('LUNA-UUID',userid)

            if isMock == 'true':
                data = utils.mock()
            else:
                data = yield utils.http_get(url, auth)

        else:
            auth = authCache[userid]
            if isMock == 'true':
                data = utils.mock()
            else:
                data = yield utils.http_get(url, auth)

        self.write(data)



