# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:28:54 2019

@author: Tarun Joshi
"""

# Create a list of absentee

n=0
with open ("absentee.txt", "wt") as wf :
    while n<26:
        entry=input("enter student name")
        if not entry:
            break
        else:
            wf.writelines(entry+"\n")
        n=n+1