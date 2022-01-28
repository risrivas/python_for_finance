#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 05:07:13 2022

@author: tanvimohan
"""


class employee:
    def __init__(self, name="Tim", emp_id=123, exp=7, dept="R&D"):
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


class subEmployee(employee):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def __init__(self, name="Tim", emp_id=123, exp=7, dept="R&D", sub_id="S001"):
        # def __init__(self, *args, **kwargs, sub_id="S001"):
        super(subEmployee, self).__init__(name, emp_id, exp, dept)
        self.Sub_ID = sub_id
        print(
            f"Employee {self.Emp_id} is created for subsidiary {self.Sub_ID}")

    def calcSalary(self):
        self.Salary = min(max(1, self.Exp) * 30000, 200000)


subEmp1 = subEmployee("Tina", 321, 6, "Marketing", "S003")
subEmp1.empDesc()
subEmp1.calcSalary()

print(subEmp1.Salary)
