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

    def mock_data(self):
        return json.dumps({"name": fake.name(), "email":fake.company_email(), "company": fake.company() })