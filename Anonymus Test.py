# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:45:05 2022

@author: ninad
"""

plugboard={21: 69, 27: 90, 23: 29, 76: 2, 65: 56, 126: 42, 1: 13, 18: 121, 101: 12, 25: 35, 28: 58, 72: 74, 105: 108, 114: 67, 86: 63, 11: 68, 78: 30, 79: 124, 33: 84, 24: 52, 43: 92, 100: 22, 16: 71, 107: 75, 122: 10, 127: 119, 55: 61, 44: 54, 60: 9, 64: 103, 83: 80, 31: 111, 0: 89, 39: 118, 51: 17, 19: 46, 50: 15, 66: 82, 6: 26, 41: 96, 94: 3, 32: 85, 20: 47, 7: 59, 106: 123, 8: 70, 34: 102, 38: 62, 87: 109, 81: 48, 91: 14, 113: 97, 95: 37, 120: 77, 112: 36, 99: 93, 125: 57, 53: 110, 117: 73, 104: 116}
def get_key(x,val):
    
    for key, value in x.items():
         if val == value:
             return key
print(get_key(plugboard, 48))