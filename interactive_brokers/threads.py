#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 08:26:41 2022

@author: tanvimohan
"""

import threading
import numpy as np
import time


def randNumGen():
    for a in range(15):
        print(np.random.randint(1, 1000))
        time.sleep(1)


thr1 = threading.Thread(target=randNumGen, daemon=True)
# thr1.daemon = True
thr1.start()


def greeting():
    for i in range(10):
        print("hello")
        time.sleep(1)


# randNumGen()
greeting()
