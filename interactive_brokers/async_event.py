#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 07:48:22 2022

@author: tanvimohan
"""

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
import time


class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print(
            f"Error reqId={reqId}, errorCode={errorCode}, errorString={errorString}")

    def contractDetails(self, reqId, contractDetails):
        print(f"reqId={reqId}, contract={contractDetails}")


def websocket_conn():
    app.run()
    event.wait()
    if event.is_set():
        app.close()


event = threading.Event()
app = TradingApp()
app.connect("127.0.0.1", 7497, clientId=1)


conn_thread = threading.Thread(target=websocket_conn)
conn_thread.start()

time.sleep(1)

contract = Contract()
contract.symbol = "AAPL"
contract.secType = "STK"
contract.currency = "USD"
contract.exchange = "SMART"

app.reqContractDetails(100, contract)

time.sleep(5)
event.set()
