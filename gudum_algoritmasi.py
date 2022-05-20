def satir_yazdir():
    satir1 = ""
    satir2 = ""
    satir3 = ""
    satir4 = ""
    satir5 = ""
    satir6 = ""

    for i in range(0,10):
        satir1 += str(alan[i])
    for i in range(10,20):
        satir2 += str(alan[i])
    for i in range(20,30):
        satir3 += str(alan[i])
    for i in range(30,40):
        satir4 += str(alan[i])
    for i in range(40,50):
        satir5 += str(alan[i])  
    for i in range(50,60):
        satir6 += str(alan[i])  
    
    print(satir1)
    print(satir2)
    print(satir3)
    print(satir4)
    print(satir5)
    print(satir6)
    print("--------------------------------------------------")
import random

alan = []
for i in range(0,60):
    alan.append("x")

#robot = random.randint(0,50)
robot_x = int(input("robot_X 1,10: ")) 
robot_satir = int(input("robot_satir 1,5: "))
cember_x = random.randint(1,10) 
cember_satir = random.randint(1,5) 
alan[(cember_satir*10)+cember_x] = "C"

while(not(((robot_x == 0) or (robot_x == 10)) and ((robot_satir <= 0) or (robot_satir >= 5)))):
    alan[robot_x+(robot_satir*10)] = "x"
    if robot_x >= 4:
        if robot_x < 10:
            if robot_x != 9:
                robot_x += 1
    else:
        if robot_x > 0:
            robot_x += -1
    if robot_satir > 3:
        if robot_satir < 5:
            robot_satir += 1
    else:
        if robot_satir > 0:
            robot_satir += -1
    print("robot satır: ",robot_satir+1)
    print("robot x",robot_x+1)
    alan[robot_x+(robot_satir*10)] = "R"
    satir_yazdir()
#robot tarama için kendini kenara yerleştiriyor
if robot_x < 5:
    robot_yon = 1
else:
    robot_yon = -1
while(not((robot_x in range(cember_x-1,cember_x+1)) and (robot_satir in range(cember_satir-1,cember_satir+1)))):
    alan[robot_x+(robot_satir*10)] = "x"    

    if robot_satir > 3:
        while(not(robot_satir == 0)):
            alan[robot_x+(robot_satir*10)] = "x"   
            robot_satir += -1
            if (robot_x in range(cember_x-1,cember_x+1)) and (robot_satir in range(cember_satir-1,cember_satir+1)):
                break
            alan[robot_x+(robot_satir*10)] = "R"
            print(robot_x+(robot_satir*10))
            satir_yazdir()
    
    else:
        while(not(robot_satir == 5)):
            alan[robot_x+(robot_satir*10)] = "x" 
            robot_satir += +1
            if (robot_x in range(cember_x-1,cember_x+1)) and (robot_satir in range(cember_satir-1,cember_satir+1)):
                break
            alan[robot_x+(robot_satir*10)] = "R"
            print(robot_x+(robot_satir*10))
            satir_yazdir()
    if not((robot_x in range(cember_x-1,cember_x+1)) and (robot_satir in range(cember_satir-1,cember_satir+1))):
        alan[robot_x+(robot_satir*10)] = "x"   
        robot_x += 1*robot_yon
        alan[robot_x+(robot_satir*10)] = "R"
        print(robot_x+(robot_satir*10))
        satir_yazdir()
    
