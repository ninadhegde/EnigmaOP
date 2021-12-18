
import random

lst2x=[0]*128    
lst2x=random.sample(range(0, 127), 120)
plugs=[-1]*128
x=1
for i in plugs:
    if i!=plugs[i]:
        x=0
if x==0:
    print('Plug Failed')
else:
    print('Success')