
import random
lst2x=[0]*128    
lst2x=random.sample(range(0, 128), 120)
plugboardx=[-1]*128
for i in range(0,119,2):
    key=lst2x[i+1]
    value=lst2x[i]
    plugboardx[key]=value
    plugboardx[value]=key
x=1
for i in plugboardx:
    if i==(-1):
        continue
    elif i==plugboardx[i]:
        x=0
    
    
    print(str(i)+'  :  '+str(plugboardx[i]))
if x==0:
    print('Plug Failed')
else:
    print('Success')
    print(plugboardx)
    print(lst2x)