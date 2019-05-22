# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:50:47 2019

@author: Tarun Joshi
"""

# Copy command

#file1=open("new.txt","rt")
#line=file1.read()
#file2=open("new1.txt","wt")
#file2.write(line)
#file2.flush

#above program uses memory buffer a lot so we use the below code

with open ("new.txt", "rt") as rf :
  with open ("empty.txt", "wt") as wf :
    for line in rf :
      wf.write (line)