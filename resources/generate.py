import random
def random_settings():
    RotorSetting=[]
    Rotor_combination=[]
    lst=[] 
    for i in range(0,350):
        lst.append(i)
        #Taking a random setting all rotors set to zero
    for i in range(0,300):
        RotorSetting.append(random.randint(0, 128))
        s=random.choice(lst)
        Rotor_combination.append(s)
        lst.remove(s)
    return Rotor_combination , RotorSetting   