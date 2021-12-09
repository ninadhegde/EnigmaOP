
import random
from resources import Rotors

x=13
y=0

RotorSet=Rotors.Rotor()
RotorSet=list(RotorSet)
PositionSet=[]
lst=[]
for i in range(0,350):
    lst.append(i)
    
    
    
#Taking a random setting all rotors set to zero
for i in range(0,300):
    s=random.choice(lst)
    PositionSet.append(s)
    lst.remove(s)
PositionSet[0]=2
print(PositionSet)   

con=x

for i in PositionSet:
    con=RotorSet[i][con]
    print(con)
print(con)