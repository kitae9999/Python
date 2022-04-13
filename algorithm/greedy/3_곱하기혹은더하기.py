given_number=input("문자열을 입력하세용 ")
numlen=len(given_number)
tempnum=int(given_number[0]) #최근계산값
#0을만나면 더하기,
for i in range(1,numlen):
    if tempnum*int(given_number[i])>tempnum+int(given_number[i]):
        tempnum=tempnum*int(given_number[i])
    else:
        tempnum=tempnum+int(given_number[i])

print(tempnum)