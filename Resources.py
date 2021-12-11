# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 18:58:05 2021

@author: ninad
"""
from Rotors import *
#importing the mechine wirings
import random


asciinumlist=[]
asciicharlist=[]
asciicharlist=['¡', '¢', '£', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', 'Æ', '®', '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '÷']
asciinumlist=[161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 198, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 247]

def random_settings():
    RotorSetting=[]
    Rotor_combination=[]
    lst=[] 
    for i in range(0,350):
        lst.append(i)
        #Taking a random setting all rotors set to zero
    for i in range(0,300):
        RotorSetting.append(random.randint(0, 128))
        s=random.choice(lst)
        Rotor_combination.append(s)
        lst.remove(s)
    return Rotor_combination , RotorSetting
def tochar(num):
    return chr(asciinumlist[num])
def tonum(char):
    return asciicharlist.index(char)

def getcharlist():
    return asciicharlist
def getnumlist():
    return asciinumlist
tple=Rotor()
wiring=list(tple)
reflector=[94, 120, 127, 77, 118, 53, 21, 126, 121, 28, 62, 98, 122, 24, 30, 109, 87, 84, 60, 41, 74, 70, 107, 39, 15, 42, 100, 50, 124, 81, 104, 57, 10, 9, 71, 83, 95, 64, 47, 99, 69, 3, 55, 17, 48, 51, 106, 76, 115, 113, 4, 2, 44, 49, 56, 36, 46, 35, 22, 119, 26, 14, 92, 125, 110, 1, 23, 123, 43, 29, 96, 59, 66, 45, 67, 108, 11, 58, 72, 16, 5, 25, 73, 7, 86, 40, 79, 80, 0, 54, 19, 88, 102, 20, 91, 105, 33, 27, 8, 68, 31, 32, 37, 117, 52, 38, 75, 111, 34, 65, 112, 61, 116, 85, 93, 13, 89, 97, 18, 78, 90, 82, 101, 12, 6, 103, 63, 114]

def runThrough(Rotor_num,input,Rotor_setting):
    input = (input+Rotor_setting) % 127;
    return wiring[Rotor_num][input];
def decrypt(Rotor_combination,RotorSetting,x):
    connectTo=x
    s=x
    
    #Deciphering block
    for i in range(299,-1,-1):
        s=runThrough(Rotor_combination[i],s,RotorSetting[i])
        connectTo=s
    s=reflector[s]
    for i in range(0,300):
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
import Rotors

#importing the mechine wirings
tple=Rotors.Rotor()
wiring=list(tple)
reflector=[94, 120, 127, 77, 118, 53, 21, 126, 121, 28, 62, 98, 122, 24, 30, 109, 87, 84, 60, 41, 74, 70, 107, 39, 15, 42, 100, 50, 124, 81, 104, 57, 10, 9, 71, 83, 95, 64, 47, 99, 69, 3, 55, 17, 48, 51, 106, 76, 115, 113, 4, 2, 44, 49, 56, 36, 46, 35, 22, 119, 26, 14, 92, 125, 110, 1, 23, 123, 43, 29, 96, 59, 66, 45, 67, 108, 11, 58, 72, 16, 5, 25, 73, 7, 86, 40, 79, 80, 0, 54, 19, 88, 102, 20, 91, 105, 33, 27, 8, 68, 31, 32, 37, 117, 52, 38, 75, 111, 34, 65, 112, 61, 116, 85, 93, 13, 89, 97, 18, 78, 90, 82, 101, 12, 6, 103, 63, 114]

def runThrough(Rotor_num,input,Rotor_setting):
    input = (input+Rotor_setting) % 127;
    return wiring[Rotor_num][input];
def encrypt(Rotor_combination,RotorSetting,x):
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
        