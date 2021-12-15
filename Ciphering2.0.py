

from Resources import *
import numpy
#importing the mechine wirings
tple=Rotor()
wiring=list(tple)

ascii_num=12
input_string=input('Enter Something for encryption')
cipher_text=''
initial_settings=[]
plugboard={}
#Rotor_combination,Rotor_Setting,plugboard=random_settings()

Rotor_combination,Rotor_Setting,plugboard=random_settings()
initial_settings.append(Rotor_combination)
initial_settings.append(Rotor_Setting)
initial_settings.append(plugboard)
for i in input_string:
    ascii_num=tonum(i)
    Rotor_combination,Rotor_Setting,ascii_num=encrypt(Rotor_combination,Rotor_Setting,plugboard,ascii_num)
    var=ascii_num
    cipher_text=cipher_text+tochar(var)
encode=cipher_text
print('Encrypted text= '+cipher_text)
print('Key = '+str(initial_settings))
x=''
x=cipher_text

Rotor_combination,Rotor_Setting,plugboard=initial_settings[0],initial_settings[1],initial_settings[2]
cipher_text=''
input_string=x
for i in input_string:
    ascii_num=tonum(i)
    Rotor_combination,Rotor_Setting,ascii_num=encrypt(Rotor_combination,Rotor_Setting,plugboard,ascii_num)
    var=ascii_num
    cipher_text=cipher_text+tochar(var)
print('Decrypted text= '+cipher_text)
print('Encrypted text= '+encode)