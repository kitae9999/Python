n=int(input("공간의 크기를 입력하세요 :"))
start_x=1
start_y=1
while True:
    command=input()
    if command=="R":
        start_y+=1
        if start_y>n:
            start_y-=1
    elif command=="L":
        start_y-=1
        if start_y<1:
            start_y+=1
    elif command=="U":
        start_x-=1
        if start_x<1:
            start_x+=1
    elif command=="D":
        start_x+=1
        if start_x>n:
            start_x-=1
    elif command=="":        
        print(start_x,start_y)     
        break
