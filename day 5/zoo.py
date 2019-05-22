# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:51:46 2019

@author: Tarun Joshi
"""

# Zoo Management


import csv
def read_zoo():
    with open ("zoo.csv") as zoo:
        list1=[]
        csv_reader=csv.reader(zoo, delimiter=",")
        for row in csv_reader:
            list1.append(row[0])
        set1= set(list1)
        for item in set1:
            print(item)
def water():
    with open ("zoo.csv") as zoo:
        dict1={}
        csv_reader=csv.reader(zoo, delimiter=",")
        for item in csv_reader:
            if item[0]=="tiger":
                key="tiger"
                if key in dict1:
                    dict1[key]=int(dict1[key])+int(item[2])
                else:
                    dict1[key]=int(item[2])
            if item[0]=="elephant":
                    key1="elephant"
                    if key1 in dict1:
                        dict1[key1]=int(dict1[key1])+int(item[2])
                    else:
                        dict1[key1]=int(item[2])
        print(dict1)  
read_zoo()        
water()   
