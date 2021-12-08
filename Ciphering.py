import random
from resources import Rotors


def rotor_sys(level,pos):
    print(level,pos)
    if level==299:
        return RotorSet[level][pos]
    
    return rotor_sys(level+1,RotorSet[level][pos])



Rotor_s=Rotors.Rotor()
lst=[]
for i in range(0,350):
    lst.append(i)


for i in range(0,50):
    x=random.choice(lst)
    lst.remove(x)
print(len(lst))
    
RotorSet=[]
for i in lst:
    RotorSet.append(Rotor_s[i])

print(len(RotorSet))   
    

x=11
y=rotor_sys(0,x)   
print(y)