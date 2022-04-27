# n=int(input())
# if 0<=n<3:
#     count=(n+1)*10*6*10*6-(n+1)*5*9*5*9
# elif 3<=n<20:
#     count=(n+1)*10*6*10*6-n*5*9*5*9
# elif 20<=n<23:
#     count=(n+1)*10*6*10*6-(n+1)*5*9*5*9

# elif n==23:
#     count=3600

# print(count)

h=int(input())

count=0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            #매 시각 안에 3이 포함되어 있다면 카운트 증가
            if '3' in str(i)+str(j)+str(k):
                count+=1

print(count)

