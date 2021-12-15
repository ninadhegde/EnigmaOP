
import random

lst2=[0]*128    
lst2=random.sample(range(0, 127), 120)
plugs=[-1]*128
for i in range(0,119,2):
    key=lst2[i+1]
    value=lst2[i]
    print(key)
    print(value)
    plugs[key]=value
    plugs[value]=key
