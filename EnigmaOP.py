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
initial_settings=[]
plugboard={}


Rotor_combination,Rotor_Setting,plugboard=generate.random_settings()
initial_settings.append(Rotor_combination)
initial_settings.append(Rotor_Setting)
initial_settings.append(plugboard)

for i in input_string:
    ascii_num=convert.tonum(i)
    Rotor_combination,Rotor_Setting,ascii_num=cipher.encrypt(Rotor_combination,Rotor_Setting,plugboard,ascii_num)
    var=ascii_num
    cipher_text=cipher_text+convert.tochar(var)
encode=cipher_text
print('Encrypted text= '+cipher_text)
print('Key = '+str(initial_settings))
x=''
x=cipher_text

Rotor_combination,Rotor_Setting,plugboard=initial_settings[0],initial_settings[1],initial_settings[2]
cipher_text=''
input_string=copyinput
for i in input_string:
    ascii_num=convert.tonum(i)
    Rotor_combination,Rotor_Setting,ascii_num=cipher.encrypt(Rotor_combination,Rotor_Setting,plugboard,ascii_num)
    var=ascii_num
    cipher_text=cipher_text+convert.tochar(var)
print('Decrypted text= '+cipher_text)
print('Encrypted text= '+encode)
print('Input text= '+copyinput)
