
import random
from resources import Rotors

def runThrough(input,position):
    input = (input+position) % 127;
    return wiring[input][1];
x=14
y=0
RotorSetting=[]
tple=Rotors.Rotor()

wiring=list(tple)
RotorPosition=[]
lst=[]
for i in range(0,350):
    lst.append(i)
    
print(len(wiring))
    
#Taking a random setting all rotors set to zero
for i in range(0,300):
    RotorSetting.append(0)
    s=random.choice(lst)
    RotorPosition.append(s)
    lst.remove(s)

print(len(RotorSetting)   )

connectTo=x
s=x
for i in range(0,300):
    s=wiring[RotorPosition[i]][connectTo]
    connectTo=s
s=connectTo
print('\n\n' + str(connectTo))
print('\n\n')
print('ASCII=')
print(chr(connectTo))
