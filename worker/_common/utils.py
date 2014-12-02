#!/usr/bin/env python
#encoding: UTF-8

import url
import json

class UrlUtils:
    def __init__(self):
        pass


class TypeUtils:
    def __init__(self):
        pass

    def loadJson(self, response):
        isJson = response.headers['content-type'].find('application/json');
        if isJson:
            return json.loads(response.text)

        