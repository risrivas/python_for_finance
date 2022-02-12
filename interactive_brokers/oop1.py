#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 05:07:13 2022

@author: tanvimohan
"""

# =============================================================================
# import math
#
# radius = 10.4
#
# def calAreaSquare(rad):
#     return math.pi * rad * rad
#
# dir(radius)
#
# =============================================================================

import os

os.chdir("/Users/tanvimohan/Desktop/algo_trading/python_for_finance/interactive_brokers")


class employee:
    def __init__(self, name="Tim", emp_id=3452, exp=6, dept="R&D"):
        self.Name = name
        self.Emp_id = emp_id
        self.Exp = exp
        self.Dept = dept
        print(f"Employee {self.Emp_id} is created")

    def calcSalary(self):
        if self.Exp > 5 and self.Dept == "R&D":
            self.Salary = 200000
        else:
            self.Salary = 80000
        print(f"Salary of {self.Name} calculated")

    def empDesc(self):
        print(
            f"Employee {self.Name} from {self.Dept} department working with us for {self.Exp} years.")


emp1 = employee("Kenneth Chin", 12345, 11, "IT")
emp1.empDesc()
emp1.calcSalary()
emp1.Salary

emp2 = employee()
emp2.calcSalary()
emp2.Salary
