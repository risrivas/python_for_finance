#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 09:28:59 2022

@author: tanvimohan
"""

import requests
import os
import json

os.chdir("/Users/tanvimohan/Desktop/algo_trading/python_for_finance/alpaca_revisited")

# url = "https://stackoverflow.com/"
endpoint = "https://paper-api.alpaca.markets"
headers = json.loads(open("key.txt", 'r').read())


# r = requests.get(url)
r = requests.get(endpoint, headers=headers)

r.text
