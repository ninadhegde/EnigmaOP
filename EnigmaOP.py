# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 13:19:38 2021
@author: ninad
"""
from resource import Rotors
from resource import cipher
from resource import connect
from resource import generate
from resource import convert
import numpy
#importing the mechine wirings
tple=Rotors.Rotor()
wiring=list(tple)

ascii_num=12
input_string=input('Enter Something for encryption')
copyinput=input_string
cipher_text=''
initialsettings=[]
plugboard={}


Rotor_combination,Rotor_Setting,plugboard=generate.random_settings()
initialsettings.append(tuple(Rotor_combination))
initialsettings.append(tuple(Rotor_Setting))
initialsettings.append(tuple(plugboard))
initial_settings=tuple(initialsettings)
for i in input_string:
    ascii_num=convert.tonum(i)
    Rotor_combination,Rotor_Setting,ascii_num=cipher.encrypt(Rotor_combination,Rotor_Setting,plugboard,ascii_num)
    var=ascii_num
#    print("var : "+str(var))
    cipher_text=cipher_text+convert.tochar(var)
encode=cipher_text
print('Encrypted text= '+cipher_text)
#print('Key = '+str(initial_settings))
x=''
x=cipher_text
Rotor_Setting=[]
Rotor_combinationx,Rotor_Settingx,plugboardx=initial_settings[0],list(initial_settings[1]),initial_settings[2]
cipher_text=''
input_string=x
for i in input_string:
    ascii_num=convert.tonum(i)
    Rotor_combinationx,Rotor_Settingx,ascii_num=cipher.encrypt(Rotor_combinationx,Rotor_Settingx,plugboard,ascii_num)
    var=ascii_num
    #print("var : "+str(var))
    cipher_text=cipher_text+convert.tochar(var)
print('Decrypted text= '+cipher_text)
print('Encrypted text= '+encode)
print('Input text= '+copyinput)
