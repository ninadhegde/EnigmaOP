# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:05:35 2022

@author: ninad
"""
import random

rotors=[]
for i in range(0,350):
    wiring={}
    
    lst1=[]
    for i in range(0,128):
        lst1.append(i)
    
    #rotor generation
    for i in range(0,128):
        x=random.choice(lst1)
        lst1.remove(x)
        wiring[i]=x
        
    rotors.append(wiring)
rotors=tuple(rotors)
print(rotors)