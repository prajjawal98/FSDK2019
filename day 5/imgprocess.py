# -*- coding: utf-8 -*-
"""
Created on Sat May 11 09:21:37 2019

@author: Tarun Joshi
"""

#Image Processing using PIL

import os
from PIL import Image
str1=input("enter file name")
try:
    img=Image.open(str1)
    img=img.convert(mode='L').save('a.jpg')
    img=Image.open("a.jpg")
    img=img.transpose(Image.ROTATE_270).save('a.jpg')
    img=Image.open("a.jpg")
    img=img.crop(box=( 0,0,160, 204))
    img.save('a.jpg')
    img=Image.open("a.jpg")
    img.thumbnail((75,75))
    img.save('a.jpg')
    img.show()
except Exception:
    print ( "File not found")