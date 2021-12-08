# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 20:15:38 2021

@author: ninad
"""
def addpos(current,pos):
    x=current+pos
    
    position1=((128+x)%128)
    if position1==0:
        return 0
    return position1
current=2
pos=125


print(addpos(current,pos))