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


endpoint = "https://data.alpaca.markets/v2"
headers = json.loads(open("key.txt", 'r').read())


symbol = "XLRE"
params = {
    "start": "2022-02-09T14:01:00Z",
    "limit": 200,
    # "end" : "2022-02-08T16:01:00Z",
    "timeframe": "15Min"
}

# single symbol
bar_url = endpoint + f"/stocks/{symbol}/bars"

r = requests.get(bar_url, headers=headers, params=params)

# r.text
data = r.json()


# multiple stocks
multi_bars_url = endpoint + "/stocks/bars"

multi_params = {
    "symbols": "AAPL,AMZN,QQQ",
    "start": "2022-02-09T14:01:00Z",
    "limit": 200,
    # "end" : "2022-02-08T16:01:00Z",
    "timeframe": "15Min"
}

r_m = requests.get(multi_bars_url, headers=headers, params=multi_params)

data_m = r_m.json()
