
import random
from resources import Rotors
from resources import convert_ascii

#importing the mechine wirings
tple=Rotors.Rotor()
wiring=list(tple)


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
        s=connectTo
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
        print(convert_ascii.tochar(s))
        print(RotorSetting) 
        