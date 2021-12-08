# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 20:15:38 2021

@author: ninad
"""
import random
lst=[]
for i in range(0,350):
    lst.append(i)


for i in range(0,50):
    x=random.choice(lst)
    lst.remove(x)

    

print(lst)