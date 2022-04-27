address=input("좌표를 입력하세요: ")
x=int(ord(address[0])-96)
y=int(address[1])

steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result=0
for step in steps:
    next_x=x+step[0]
    next_y=y+step[1]

    if next_x>=1 and next_x<=8 and next_y>=1 and next_y <=8:
        result+=1

print(result)
