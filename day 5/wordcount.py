# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:28:14 2019

@author: Tarun Joshi
"""

#Word Count

str1=input("enter file name")
with open (str1, "rt") as file :
    i=0
    for item in file:
        i=i+1
    print("number of lines",i)
    file.seek(0,0)
    line=list(file.read())
    print("number of characters including whitespaces",len(line))
    i=0
    for item in line:
        if item!=" " and item!="\n":
            i=i+1
    print("number of characters without including whitespaces",i)
    set1=set(line)
    print("number of unique words",len(set1))