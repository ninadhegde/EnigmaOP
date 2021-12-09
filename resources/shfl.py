# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 14:14:34 2021

@author: ninad
"""
import random
def shfl():
    lst=[]
    for i in range(0,128):
        lst.append(i)
    random.shuffle(lst)
      # lst.remove(x)
    return lst
    
