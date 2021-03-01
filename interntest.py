x=0
y=0
#1=W 2=N 3=E 4=S
direction=2
count=0
an_integer=0
command =input()
while(count<len(command)):
    
    if(command[count]=='R'):
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
    elif(command[count]=='L'):
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
    elif(command[count]=='W'):
        w_count=count+1
        integers=[]
        while(command[w_count].isnumeric()==True):
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
        if(direction==2):
            i=0
            while i< an_integer:
                y+=1
                i+=1
                if(y==0):
                    f = open("XY_Location.txt", "a")
                    f.writelines("x="+str(x)+"y="+str(y)+"\n")
                    f.close()
            
        elif(direction==3):
            i=0
            while i< an_integer:
                x+=1
                i+=1
                if(x==0):
                    f = open("XY_Location.txt", "a")
                    f.writelines("x="+str(x)+"y="+str(y)+"\n")
                    f.close()
        elif(direction==1):
            i=0
            while i< an_integer:
                x-=1
                i+=1
                if(x==0):
                    f = open("XY_Location.txt", "a")
                    f.writelines("x="+str(x)+"y="+str(y)+"\n")
                    f.close()
            
        elif(direction==4):
            i=0
            while i< an_integer:
                y-=1
                i+=1
                if(y==0):
                    f = open("XY_Location.txt", "a")
                    f.writelines("x="+str(x)+"y="+str(y)+"\n")
                    f.close()
        else:
            print("Forward Error")
        print(x,y)
        f = open("Moving_Location.txt", "a")
        f.writelines("x="+str(x)+"y="+str(y)+"\n")
        f.close()
    count+=1
    
          





