#!/usr/bin/env python3.4
#encoding: UTF-8
#

'''
generator handlers

'''

from app.models import lines
from app.handlers.base import PageHandler, XHRHandler

from tornado import gen
import json


class MainPageHandler(PageHandler):

    @gen.coroutine
    def get(self):
        result = yield lines.find_all()
        savedLines = list()
        if result['success'] == True:
            savedLines = result['data']
        self._render('index.html', savedLines=savedLines,)


class LineSave(XHRHandler):

    @gen.coroutine
    def post(self):
        url = self.get_body_argument('url')
        rule = self.get_body_argument('rule')

        response = yield lines.save({'url':url, 'rule':rule})
        self._write_json(response)


class LineRemove(XHRHandler):

    @gen.coroutine
    def get(self):
        url = self.get_argument('url')

        response = yield lines.remove({'url':url})
        self._write_json(response)


class LineSearch(XHRHandler):
    @gen.coroutine
    def get(self):
        url = self.get_argument('url')

        response = yield lines.find_one({'url':url})
        self._write_json(response)
