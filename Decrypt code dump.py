# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 20:57:17 2021

@author: ninad
"""

def decrypt(Rotor_combination,RotorSetting,x):
    connectTo=x
    s=x
    
    #ciphering block
    for i in range(0,300):
        s=runThrough(Rotor_combination[i],s,RotorSetting[i])
        connectTo=s
    s=reflector[s]
    for i in range(299,-1,-1):
        s=runThrough(Rotor_combination[i],s,RotorSetting[i])
        connectTo=s
    triger=1
    counter=0
    #incrementing the 1st rotor setting by 1     
    while triger==1:
        RotorSetting[counter]+=1
        if RotorSetting[counter]>127:
            RotorSetting[counter]=0
        else:
            triger=0
        counter+=1
        
    return Rotor_combination,RotorSetting,connectTo 

