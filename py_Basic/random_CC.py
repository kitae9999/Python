from random import *

print(random()) #0.0~1.0 미만의 임의의 값 생성
print(random()*10)#0.0~10.0 미만의 임의의 값 생성
print(int(random()*10))#0~10 미만의 임의의 값 생성
print(int(random()*10+1))#1~11 미만의 임의의 값 생성

time=randrange(5,51) #5~50까지 숫자중 랜덤