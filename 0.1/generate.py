# -*- coding: utf-8 -*-
"""
Created on Sat May  7 21:10:41 2022

@author: ninad
"""

import random
def random_settings():
    RotorSetting=[]
    Rotor_combination=[]
    lst=[] 
    for i in range(0,3):
        lst.append(i)
        #Taking a random setting all rotors set to zero
    for i in range(0,3):
        RotorSetting.append(random.randint(0, 3))
        s=random.choice(lst)
        Rotor_combination.append(s)
        lst.remove(s)
    return Rotor_combination , RotorSetting   