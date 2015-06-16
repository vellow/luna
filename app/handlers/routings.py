#!/usr/bin/env python3.4
#encoding: UTF-8
#

'''
routing register

'''

from app.handlers import MainHandlers, MockHandlers
import tornado.web

handlers = [
    ("/", MainHandlers.MainPageHandler),
    ("/line/save", MainHandlers.LineSave),
    ("/line/remove", MainHandlers.LineRemove),
    ("/search", MainHandlers.LineSearch),
    ("/real", MockHandlers.MockHandler),
    (r'/static', tornado.web.StaticFileHandler, {'path': '/'}),
]



