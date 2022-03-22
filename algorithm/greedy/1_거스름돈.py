n = int(input("거스름돈이 총 얼마 남았나요?"))
count = 0
array = [500,100,50,10]
for coin in array:
    count +=n//coin
    n %= coin

print(count)
