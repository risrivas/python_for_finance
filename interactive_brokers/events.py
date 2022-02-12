#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 08:26:41 2022

@author: tanvimohan
"""

import threading
import time


def NumGen():
    for a in range(30):
        if event.is_set():
            break
        else:
            print(a)
            time.sleep(1)


event = threading.Event()

thr1 = threading.Thread(target=NumGen)
# thr1.daemon = True
thr1.start()


def greeting():
    for i in range(10):
        print("hello")
        time.sleep(1)


greeting()
event.set()
# event.clear()
