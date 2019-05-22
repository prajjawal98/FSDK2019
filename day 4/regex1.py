# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:08:52 2019

@author: Tarun Joshi
"""

# Regular Expression 1

import re
str1=input("enter the string")
li=str1.split(" ")
for val in li:
 if val == re.match(r"[-+]?\d*\.\d+$",string_N):
     print ('true')
 else:
     print ('false')
