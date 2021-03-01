######################################
x=0
y=0
#1=W 2=N 3=E 4=S   
direction=2
Current_direction=['West','North','East','South']
count=0
an_integer=0
######################################
#โปรแกรมเป็นแบบเรียกใช้รอบเดียว ป้อนคำสั่งรอบเดียวครับ ไม่ได้ใส่Loopให้ป้อนหลายรอบ
command =input()     #รับค่าInput
while(count<len(command)):      #Check input
    if(command[count]=='R'):    #Change Direction
        if(direction==2):
            direction=3
        elif(direction==1):
            direction=2
        elif(direction==3):
            direction=4
        elif(direction==4):
            direction=1
        else:
            print("Direction Error")
    elif(command[count]=='L'):   #Change Direction
        if(direction==2):
            direction=1
        elif(direction==1):
            direction=4
        elif(direction==3):
            direction=2
        elif(direction==4):
            direction=3
        else:
            print("Direction Error")
    elif(command[count]=='W'): #Forwarding
        w_count=count+1
        integers=[]
        while(command[w_count].isnumeric()==True): #Check num
            integers.append(command[w_count])
            w_count+=1
            if(w_count>=len(command)):
                strings = [str(integer) for integer in integers]
                a_string = "".join(strings)
                an_integer = int(a_string)
                break
            elif(command[w_count].isnumeric()==False):
                strings = [str(integer) for integer in integers]
                a_string = "".join(strings)
                an_integer = int(a_string)
                break
        if(direction==2):  #Forward Condition1
            i=0
            while i< an_integer:
                y+=1
                i+=1
                if(y==0):
                    f = open("XY_Location.txt", "a")        #write txt
                    f.writelines("x="+str(x)+"y="+str(y)+"\n")
                    f.close()
            
        elif(direction==3): #Forward Condition2
            i=0
            while i< an_integer:
                x+=1
                i+=1
                if(x==0):
                    f = open("XY_Location.txt", "a")         #write txt
                    f.writelines("x="+str(x)+"y="+str(y)+"\n")
                    f.close()
        elif(direction==1): #Forward Condition3
            i=0
            while i< an_integer:
                x-=1
                i+=1
                if(x==0):
                    f = open("XY_Location.txt", "a")         #write txt
                    f.writelines("x="+str(x)+"y="+str(y)+"\n")
                    f.close()
            
        elif(direction==4): #Forward Condition4
            i=0
            while i< an_integer:
                y-=1
                i+=1
                if(y==0):
                    f = open("XY_Location.txt", "a")         #write txt
                    f.writelines("x="+str(x)+"y="+str(y)+"\n")
                    f.close()
        else:
            print("Forward Error")
        f = open("Moving_Location.txt", "a")             #write txt
        f.writelines("x="+str(x)+"y="+str(y)+"\n")
        f.close()
    count+=1
print("Current Position After Commanded : X=",x,",Y=",y,",Direction=",Current_direction[direction-1]) #Show Current Position

    
          





