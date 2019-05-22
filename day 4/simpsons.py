# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:18:44 2019

@author: Tarun Joshi
"""

import re
with open('simpsons_phone_book.txt', mode='rt') as file :
    str1=file.read()
    list1=str1.split(" ")
    print(list1)
    for item in list1:
        a=re.search(r'[Neu]$',item)
        print(a)
    