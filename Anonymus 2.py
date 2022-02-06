
import Rotors
wiring=Rotors.Rotor()
RotorSettingopz=[]
def runThrough(Rotor_num,inputy,Rotor_settingy):
    inputy = (inputy+Rotor_settingy) % 127;
    return wiring[Rotor_num][inputy];
def plug(plugboard,key):
    if plugboard[key]==(-1):
        return key
    else:
        return plugboard[key]
reflector=[127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
def encrypt(Rotor_combinationz,RotorSettingz,plugboardz,x):
    print('before plugging = '+str(x))
    x=plug(plugboardz,x)
    connectTo=x
    s=x
    print('after plugging = '+str(x))
    #ciphering block
    for i in range(0,2):
        print('before roter : '+str(i)+' = '+str(s))
        s=runThrough(Rotor_combinationz[i],s,RotorSettingz[i])
        connectTo=s
        print('after roter : '+str(i)+' = '+str(s))
    #s=reflector[s]
    print('\n_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n')
    for i in range(1,-1,-1):
        print('before roterRevr : '+str(i)+' = '+str(s))
        
        s=runThrough(Rotor_combinationz[i],s,RotorSettingz[i])
        connectTo=s
        print('after roterRevr : '+str(i)+' = '+str(s))
    print('before plugging = '+str(connectTo))
    connectTo=plug(plugboardz,connectTo)
    print('after plugging = '+str(connectTo))
    triger=1
    counter=0
    
    #incrementing the 1st rotor setting by 1     
    while triger==1 and counter<300:
        RotorSettingz[counter]+=1
        if RotorSettingz[counter]>127:
            RotorSettingz[counter]=0
        else:
            triger=0
        counter+=1
        RotorSettingopz=RotorSettingz
        RotorSettingz=[]
    return Rotor_combinationz,RotorSettingopz,connectTo
ascii_num=78
Rotor_combination=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299]
Rotor_Setting=[0]*300
plugboard=[15, 117, 27, 56, 102, 79, 124, 73, 13, 39, 91, 40, 108, 8, 126, 0, 20, 78, 59, 87, 16, 31, 99, 100, 36, 113, 65, 2, 77, 57, -1, 21, 119, 98, 63, 47, 24, 82, 121, 9, 11, 93, 89, 52, 49, 68, 75, 35, 101, 44, 88, 123, 43, 127, 61, 107, 3, 29, 66, 18, -1, 54, -1, 34, 70, 26, 58, -1, 45, 94, 64, 104, 116, 7, 111, 46, 110, 28, 17, 5, -1, -1, 37, 85, 106, 83, 105, 19, 50, 42, 112, 10, -1, 41, 69, 120, -1, 103, 33, 22, 23, 48, 4, 97, 71, 86, 84, 55, 12, 118, 76, 74, 90, 25, 115, 114, 72, 1, 109, 32, 95, 38, 125, 51, 6, 122, 14, 53]
Rotor_combination,Rotor_Setting,ascii_num=encrypt(Rotor_combination,Rotor_Setting,plugboard,ascii_num)