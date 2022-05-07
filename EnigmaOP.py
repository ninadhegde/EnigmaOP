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
'''
Rotor_combination=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299]
Rotor_Setting=[0]*300
plugboard={21: 69, 27: 90, 23: 29, 76: 2, 65: 56, 126: 42, 1: 13, 18: 121, 101: 12, 25: 35, 28: 58, 72: 74, 105: 108, 114: 67, 86: 63, 11: 68, 78: 30, 79: 124, 33: 84, 24: 52, 43: 92, 100: 22, 16: 71, 107: 75, 122: 10, 127: 119, 55: 61, 44: 54, 60: 9, 64: 103, 83: 80, 31: 111, 0: 89, 39: 118, 51: 17, 19: 46, 50: 15, 66: 82, 6: 26, 41: 96, 94: 3, 32: 85, 20: 47, 7: 59, 106: 123, 8: 70, 34: 102, 38: 62, 87: 109, 81: 48, 91: 14, 113: 97, 95: 37, 120: 77, 112: 36, 99: 93, 125: 57, 53: 110, 117: 73, 104: 116}
'''
Rotor_Setting=[0]*300

initialsettings.append(tuple(Rotor_combination))
initialsettings.append(tuple(Rotor_Setting))
initialsettings.append(tuple(plugboard))
initial_settings=tuple(initialsettings)
for i in input_string:
    
    ascii_num=convert.tonum(i)
    print("var : "+str(ascii_num))
    Rotor_combination,Rotor_Setting,ascii_num=cipher.encrypt(Rotor_combination,Rotor_Setting,plugboard,ascii_num)
    var=ascii_num
    print("var : "+str(var))
    cipher_text=cipher_text+convert.tochar(var)
encode=cipher_text
#print('Encrypted text= '+cipher_text)
print('----------------------------------')
#print('Key = '+str(initial_settings))
x=''
x=cipher_text
Rotor_Setting=[]
Rotor_combinationx,Rotor_Settingx,plugboardx=initial_settings[0],list(initial_settings[1]),initial_settings[2]
cipher_text=''
input_string=x
for i in input_string:
    ascii_num=convert.tonum(i)
    print("var char: "+str(ascii_num))
    Rotor_combinationx,Rotor_Settingx,ascii_num=cipher.decrypt(Rotor_combinationx,Rotor_Settingx,plugboard,ascii_num)
    var=ascii_num
    print("var : "+str(var))
    cipher_text=cipher_text+convert.tochar(var)

print(initialsettings)
print('Input text= '+copyinput)
print('Encrypted text= '+encode)
print('Decrypted text= '+cipher_text)