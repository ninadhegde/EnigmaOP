# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 12:48:48 2021

@author: ninad
"""

asciinumlist=[]
asciicharlist=['a','b','c','d','e','f','g','h','i']
asciinumlist=[1,2,3,4,5,6,7,8,9]
reflector=[9,8,7,6,5,4,3,2,1]
def tochar(num):
    return chr(asciinumlist[num])
def tonum(char):
    return asciicharlist.index(char)
def getcharlist():
    return asciicharlist
def getnumlist():
    return asciinumlist