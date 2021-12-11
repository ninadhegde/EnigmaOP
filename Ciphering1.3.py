
import random
from resources import Rotors
from resources import convert_ascii

def runThrough(Rotor_num,input,Rotor_setting):
    input = (input+Rotor_setting) % 127;
    return wiring[Rotor_num][input];
x=2
y=0
RotorSetting=[]
tple=Rotors.Rotor()

wiring=list(tple)
Rotor_combination=[]
lst=[]
for i in range(0,350):
    lst.append(i)
    
print(len(wiring))
"""   
#Taking a random setting all rotors set to zero
for i in range(0,300):
    RotorSetting.append(0)
    s=random.choice(lst)
    RotorPosition.append(s)
    lst.remove(s)
"""
for i in range(6,306):
    RotorSetting.append(0)
    
    Rotor_combination.append(i)
RotorSetting[0]=12
RotorSetting[5]=1
RotorSetting[299]=120
print(RotorSetting)   

connectTo=x
s=x
f=0
for i in range(0,300):
    s=runThrough(Rotor_combination[i],s,RotorSetting[i])
    print(str(Rotor_combination[i])+':::'+str(s))
    connectTo=s
s=connectTo
print('\n\n' + str(connectTo))
print(convert_ascii.tochar(s))
