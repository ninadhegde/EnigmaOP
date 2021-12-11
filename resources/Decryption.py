

from resources import Rotors


#importing the mechine wirings
tple=Rotors.Rotor()
wiring=list(tple)
reflector=[94, 120, 127, 77, 118, 53, 21, 126, 121, 28, 62, 98, 122, 24, 30, 109, 87, 84, 60, 41, 74, 70, 107, 39, 15, 42, 100, 50, 124, 81, 104, 57, 10, 9, 71, 83, 95, 64, 47, 99, 69, 3, 55, 17, 48, 51, 106, 76, 115, 113, 4, 2, 44, 49, 56, 36, 46, 35, 22, 119, 26, 14, 92, 125, 110, 1, 23, 123, 43, 29, 96, 59, 66, 45, 67, 108, 11, 58, 72, 16, 5, 25, 73, 7, 86, 40, 79, 80, 0, 54, 19, 88, 102, 20, 91, 105, 33, 27, 8, 68, 31, 32, 37, 117, 52, 38, 75, 111, 34, 65, 112, 61, 116, 85, 93, 13, 89, 97, 18, 78, 90, 82, 101, 12, 6, 103, 63, 114]

def runThrough(Rotor_num,input,Rotor_setting):
    input = (input+Rotor_setting) % 127;
    return wiring[Rotor_num][input];
def encrypt(Rotor_combination,RotorSetting,x):
    connectTo=x
    s=x
    
    #ciphering block
    for i in range(0,300):
        s=runThrough(Rotor_combination[i],s,RotorSetting[i])
        connectTo=s
    s=reflector[s]
    for i in range(299,-1,-1):
        s=runThrough(Rotor_combination[i],s,RotorSetting[i])
        connectTo=s
    triger=1
    counter=0
    #incrementing the 1st rotor setting by 1     
    while triger==1:
        RotorSetting[counter]+=1
        if RotorSetting[counter]>127:
            RotorSetting[counter]=0
        else:
            triger=0
        counter+=1
        
        return Rotor_combination,RotorSetting,connectTo 
        