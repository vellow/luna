#!/usr/bin/env python
#encoding: UTF-8

'''
Generate dummy data

'''

import json
from faker import Faker

fake = Faker()

class Mock:
    def __init__(self):
        pass

    # @ rules { string }
    def mock_data(self, rules):
        rules = json.loads(rules)
        data = dict()
        for item in rules:
            for j in item:  
                # {{fake.name()}} --> fake.name()
                func = item[j][2:-2]
                data[j] = eval('fake.' + func)

        return json.dumps(data)


