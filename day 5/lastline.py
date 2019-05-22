# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:30:08 2019

@author: Tarun Joshi
"""

# Last line

str1=input("enter file name: ")
with open(str1, mode='rt') as file :
   file_contents = file.readlines()
   print (file_contents[-1])
