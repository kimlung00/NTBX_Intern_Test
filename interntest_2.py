######################################
x=0
y=0
#1=W 2=N 3=E 4=S   
direction=2
Current_direction=['West','North','East','South']
count=0
an_integer=0
######################################
def validate(x):
    i=0
    while(i<len(x)):
        if x[0].isnumeric()==True:
            return False
        elif x[i].isnumeric()!=True:
            if x[i]!="R":
                if x[i]!="L":
                    if x[i]!="W":
                        return False
        if x[i]=="W":
            if i+1<len(x):
                if x[i+1].isnumeric()!=True:
                    return False
        elif x[i]=="R":
            if i+1<len(x):
                if x[i+1].isnumeric()==True:
                    return False
        elif x[i]=="L":
            if i+1<len(x):
                if x[i+1].isnumeric()==True:
                    return False
        i+=1
    return True
def turn_right(x):
    x+=1
    if (x>4) :
        return 1
    return x
def turn_left(x):
    x-=1
    if (x<1) :
        return 4
    return x
def writeXY(x,y):
    f = open("XY_Location.txt", "a")         #write txt
    f.writelines("x="+str(x)+"y="+str(y)+"\n")
    f.close()
def writeMoving(x,y):
    f = open("Moving_Location.txt", "a")             #write txt
    f.writelines("x="+str(x)+"y="+str(y)+"\n")
    f.close()
def forward_y(a,b,integer,direct):
    if(direct == 2):
        if(b < 0 and integer >= b): 
            writeXY(int(a),0)
        return integer
    elif(direct == 4):
        if(b > 0 and integer >= b):
            writeXY(int(a),0)
        return -integer
    return 0
def forward_x(a,b,integer,direct):
    if(direct == 3):
        if(a < 0 and integer >= a): 
            writeXY(0,int(b))
        return integer
    elif(direct == 1):
        if(a > 0 and integer >= a):
            writeXY(0,int(b))
        return -integer
    return 0
#####################################
#โปรแกรมเป็นแบบเรียกใช้รอบเดียว ป้อนคำสั่งรอบเดียวครับ ไม่ได้ใส่Loopให้ป้อนหลายรอบ แต่มีValidate สำหรับให้ป้อนInputใหม่หากป้อนผิดคำสั่ง 
while True:     #รับค่าInput by Validate input
    command=input()
    if validate(command) != True:
        print("Wrong Command!!")
        continue
    else:
        break    
while(count<len(command)):      #Check input
    if(command[count]=='R'):    #Change Direction
       direction = turn_right(direction) 
    elif(command[count]=='L'):   #Change Direction
        direction = turn_left(direction)
    elif(command[count]=='W'): #Forwarding
        an_integer = 0
        while(command[count+1].isnumeric()==True): #Check 
            count+=1
            an_integer += int(command[count])
            an_integer *= 10
            if(count+1>=len(command)):
                break
        an_integer /= 10
        y += forward_y(x,y,an_integer,direction)
        x += forward_x(x,y,an_integer,direction)
        writeMoving(x,y)
    count+=1
print("Current Position After Commanded : X=",int(x),",Y=",int(y),",Direction=",Current_direction[direction-1]) #Show Current Position


    
          





