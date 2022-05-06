def get_key(x,val):
    for key, value in x.items():
         if val == value:
             return key

x={1:2,3:4}
print(get_key(x,2))
print(type(x))


