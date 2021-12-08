# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 20:15:38 2021

@author: ninad
"""

import random
lst=[]
for i in range(0,128):
    lst.append(i)

R1=[]
x=1
lst2=lst
print(lst)
for i in range(0,2):
    random.shuffle(lst)
      # lst.remove(x)
    R1.append(lst)
print(R1)