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
Rotor_combination=[333, 334, 268, 42, 164, 219, 122, 145, 56, 338, 121, 125, 196, 246, 163, 5, 70, 92, 116, 215, 106, 148, 261, 324, 204, 314, 277, 60, 94, 33, 330, 270, 7, 243, 284, 174, 267, 80, 14, 123, 325, 129, 157, 101, 97, 306, 291, 18, 34, 158, 114, 45, 331, 221, 58, 322, 249, 37, 320, 189, 239, 208, 72, 55, 51, 340, 254, 93, 2, 181, 102, 294, 20, 59, 171, 38, 247, 265, 144, 15, 126, 13, 210, 343, 68, 154, 319, 269, 199, 143, 63, 185, 43, 235, 139, 276, 138, 242, 95, 177, 341, 165, 85, 275, 50, 238, 301, 146, 128, 220, 23, 111, 35, 127, 207, 71, 40, 107, 24, 309, 280, 142, 271, 299, 310, 104, 288, 312, 133, 170, 16, 272, 62, 274, 172, 113, 83, 21, 214, 337, 186, 344, 152, 178, 302, 19, 91, 231, 289, 345, 136, 82, 323, 264, 244, 75, 118, 90, 109, 169, 285, 258, 290, 99, 77, 48, 61, 153, 81, 200, 105, 73, 240, 339, 342, 98, 346, 328, 237, 241, 305, 194, 52, 329, 228, 252, 100, 201, 168, 25, 317, 226, 257, 29, 39, 110, 292, 303, 224, 184, 4, 119, 203, 300, 22, 112, 227, 8, 304, 137, 234, 176, 197, 190, 182, 205, 283, 179, 167, 191, 347, 88, 6, 141, 326, 311, 297, 36, 180, 27, 54, 10, 149, 211, 217, 26, 1, 66, 293, 166, 65, 198, 336, 117, 86, 307, 134, 232, 160, 67, 335, 31, 278, 131, 262, 79, 132, 225, 230, 209, 248, 161, 159, 173, 218, 193, 195, 140, 253, 212, 255, 147, 0, 17, 46, 236, 266, 156, 348, 321, 124, 53, 103, 315, 245, 9, 11, 89, 49, 213, 313, 120, 318, 256, 74, 183, 296, 259, 44, 216]
Rotor_Setting=[55, 47, 124, 12, 49, 45, 124, 74, 58, 26, 11, 82, 8, 44, 109, 104, 81, 59, 118, 113, 73, 87, 2, 53, 115, 44, 25, 53, 116, 41, 30, 46, 84, 97, 120, 74, 82, 100, 32, 44, 50, 93, 81, 68, 111, 63, 60, 22, 12, 19, 4, 2, 9, 15, 94, 109, 39, 122, 96, 103, 17, 113, 107, 14, 91, 114, 0, 121, 53, 61, 108, 102, 75, 109, 27, 33, 49, 118, 126, 109, 88, 126, 37, 97, 44, 52, 117, 42, 32, 22, 50, 44, 26, 41, 4, 104, 13, 18, 108, 127, 8, 61, 66, 66, 10, 7, 121, 100, 15, 1, 83, 109, 40, 39, 81, 21, 84, 34, 107, 104, 30, 72, 80, 11, 27, 45, 36, 10, 81, 91, 100, 53, 86, 115, 37, 119, 126, 78, 8, 33, 111, 3, 97, 110, 121, 16, 96, 31, 67, 43, 67, 8, 126, 112, 25, 10, 73, 88, 115, 35, 80, 61, 17, 10, 7, 124, 41, 99, 41, 50, 31, 29, 71, 85, 82, 65, 110, 0, 56, 16, 33, 8, 63, 33, 87, 92, 43, 72, 108, 26, 93, 116, 78, 115, 95, 74, 57, 88, 41, 50, 51, 94, 29, 85, 45, 41, 118, 97, 17, 28, 45, 13, 0, 116, 109, 27, 86, 114, 39, 25, 41, 77, 91, 22, 104, 114, 37, 35, 80, 114, 121, 110, 38, 54, 44, 12, 58, 31, 39, 55, 49, 23, 53, 13, 23, 60, 56, 98, 96, 51, 46, 40, 115, 112, 127, 55, 88, 121, 30, 40, 10, 37, 26, 62, 49, 53, 33, 57, 72, 107, 126, 85, 62, 30, 9, 29, 117, 28, 113, 121, 49, 85, 84, 32, 61, 75, 11, 37, 94, 89, 24, 17, 66, 23, 112, 3, 90, 78, 69, 79]
plugboard=[22, 117, 15, 39, 61, 80, 12, 113, 26, 35, 115, 116, 6, 86, 77, 2, 105, 41, -1, 50, 58, 24, 0, 32, 21, 94, 8, 57, 104, 118, 66, 127, 23, 81, -1, 9, 119, 108, 47, 3, 91, 17, 110, 59, 87, 90, 71, 38, 109, 123, 19, -1, 97, 101, 99, 74, 89, 27, 20, 43, 95, 4, 85, -1, -1, 103, 30, -1, 78, 125, 82, 46, 93, 75, 55, 73, 122, 14, 68, -1, 5, 33, 70, 124, 100, 62, 13, 44, 92, 56, 45, 40, 88, 72, 25, 60, 121, 52, -1, 54, 84, 53, 111, 65, 28, 16, 120, 126, 37, 48, 42, 102, 114, 7, 112, 10, 11, 1, 29, 36, 106, 96, 76, 49, 83, 69, 107, 31]
#Rotor_combination,Rotor_Setting,plugboard=generate.random_settings()
initial_settings.append(Rotor_combination)
initial_settings.append(Rotor_Setting)
initial_settings.append(plugboard)
print('Key = '+str(initial_settings))
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
input_string=x
for i in input_string:
    ascii_num=convert.tonum(i)
    Rotor_combination,Rotor_Setting,ascii_num=cipher.encrypt(Rotor_combination,Rotor_Setting,plugboard,ascii_num)
    var=ascii_num
    cipher_text=cipher_text+convert.tochar(var)
print('Decrypted text= '+cipher_text)
print('Encrypted text= '+encode)
print('Input text= '+copyinput)
