from re import L


keyword=input("문자열을 입력하세요 :")
count=0
list_keyword=list()
for i in range(len(keyword)) :
   for num in range(1,10):
       if keyword[i]==str(num):
           count+=int(keyword[i])

for i in range(len(keyword)):
    for num in range(1,10):
        if keyword[i]==str(num):  #키워드[i]가 숫자라면 break
            break
    else :
        list_keyword.append(keyword[i])  

            
     

list_keyword.sort()

for i in range(len(list_keyword)):
    print (list_keyword[i],end="")
print(count)
        