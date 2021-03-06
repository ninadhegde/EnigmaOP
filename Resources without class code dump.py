# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 20:58:27 2021

@author: ninad
"""

tple=Rotor()
wiring=list(tple)

asciinumlist=[]
asciicharlist=[]
asciicharlist=['¡', '¢', '£', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', 'Æ', '®', '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '÷']
asciinumlist=[161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 198, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 247]
reflector=[127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def random_settings():
    RotorSettingx=[]
    Rotor_combinationx=[]
    lstx=[] 
    for i in range(0,350):
        lstx.append(i)
        #Taking a random setting all rotors set to zero
    for i in range(0,300):
        RotorSettingx.append(random.randint(0, 127))
        s=random.choice(lstx)
        Rotor_combinationx.append(s)
        lstx.remove(s)
    lst2x=[0]*128    
    lst2x=random.sample(range(0, 128), 120)
    plugboardx=[-1]*128
    for i in range(0,119,2):
        key=lst2x[i+1]
        value=lst2x[i]
        plugboardx[key]=value
        plugboardx[value]=key
    return Rotor_combinationx , RotorSettingx , plugboardx
def tochar(num):
    return chr(asciinumlist[num])
def tonum(char):
    return asciicharlist.index(char)

def getcharlist():
    return asciicharlist
def getnumlist():
    return asciinumlist


def runThrough(Rotor_num,inputy,Rotor_settingy):
    inputy = (inputy+Rotor_settingy) % 127;
    return wiring[Rotor_num][inputy];
def plug(plugboard,key):
    if plugboard[key]==(-1):
        return key
    else:
        return plugboard[key]



def encrypt(Rotor_combinationz,RotorSettingz,plugboardz,x):
    x=plug(plugboardz,x)
    connectTo=x
    s=x
    
    #ciphering block
    for i in range(0,300):
        s=runThrough(Rotor_combinationz[i],s,RotorSettingz[i])
        connectTo=s
    s=reflector[s]
    for i in range(299,-1,-1):
        s=runThrough(Rotor_combinationz[i],s,RotorSettingz[i])
        connectTo=s
    triger=1
    counter=0
    connectTo=plug(plugboardz,connectTo)
    #incrementing the 1st rotor setting by 1     
    while triger==1:
        RotorSettingz[counter]+=1
        if RotorSettingz[counter]>127:
            RotorSettingz[counter]=0
        else:
            triger=0
        counter+=1
        
    return Rotor_combinationz,RotorSettingz,connectTo 