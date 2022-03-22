from random import *
count=0
for passenger in range(1,51):
    time=int(random()*46+5)
    if(time>=5 and time<=15):
        check="o"
        count=count+1
    else:
        check=" "
    print("[{2}] {0}번째 손님 (소요시간 : {1}분)".format(passenger,time,check))

print("총 탑승 승객: {} 분".format(count))