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


#Rotor_combination,Rotor_Setting,plugboard=generate.random_settings()
Rotor_combination=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299]
Rotor_Setting=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
plugboard=[14, -1, 109, 19, 115, 108, 41, 71, 59, 50, 110, 22, 40, 56, 0, 122, 28, 73, 66, 3, 64, 123, 11, 86, 80, 102, 119, 43, 16, 127, 99, 62, 116, 93, 36, 42, 34, 72, 70, 107, 12, 6, 35, 27, 68, -1, 84, 82, 111, 100, 9, 78, 112, 94, 57, 104, 13, 54, -1, 8, 106, 126, 31, 67, 20, 90, 18, 63, 44, 114, 38, 7, 37, 17, -1, 77, 118, 75, 51, -1, 24, 103, 47, 96, 46, -1, 23, 97, 117, 95, 65, 101, 121, 33, 53, 89, 83, 87, 105, 30, 49, 91, 25, 81, 55, 98, 60, 39, 5, 2, 10, 48, 52, 124, 69, 4, 32, 88, 76, 26, -1, 92, 15, 21, 113, -1, 61, 29]
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
