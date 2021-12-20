def tostring(lst):
    li=''
    for i in range(0,len(lst)):
        li=li+str(lst[i])
        if i+1<len(lst):
            li=li+','
    return li

def fromstring(string):
    li = list(string.split(","))
    return li
lsty=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
strng=tostring(lsty)
op=fromstring(strng)
print(op)
print(strng)