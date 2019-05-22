# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:49:12 2019

@author: Tarun Joshi
"""

str1=input("enter credit card number")
list1=str1.split("")
if len(list1)!=16:
    print("invalid")
else:
    for item in list1:
        if item==', ' or '_':
            print("invalid")
            
    