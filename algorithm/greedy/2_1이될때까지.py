n=int(input("n의 값은 ? :"))
k=int(input("k의 값은 ? :"))
count=0
num=n%k
# def min():
#     n=n-1

# def div():
#     n=n//k

# for i in range(1,num+1):
div_num=0
kmul=n-num
# n-num #k의 배수값
while (1):
    
    div_num+=1
    if  kmul//k==1:
        break
    else:
        kmul=kmul//k
        if kmul//k>0:
            div_num=div_num+(kmul%k)
            kmul=kmul-(kmul%k)
        else: #kmul을  k로 더 이상 나눌수없는경우 = kmul이 k보다 작은 경우
            div_num=div_num+(kmul-1)
            break
count=num+div_num

print(count)

# #answer code
# n,k=map(int,input().split())
# result = 0
# while True:
#     # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
#     target=(n//k)*k
#     result+=n-target
#     n=target
#     #n이 k보다 작을때 반복문 탈출
#     if n<k:
#         break
#     #k로 나누기
#     result +=1
#     n//=k

#     #마지막으로 남은 수에 대하여 1씩 빼기
# result +=n-1
# print(result)