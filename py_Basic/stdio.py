# print("Python","java",sep=",")
# print("Python","java")
# print("Python","java",sep=" vs ")

# print("Python","java",sep=",",end="?") #end의 디폴트는 줄바꿈
# import sys
# print("Python","Java",file=sys.stdout)
# print("Python","Java",file=sys.stderr)

# scores={"수학":0,"영어":50,"코딩":100}
# for subject,score in scores.items():
#     # print(subject,score)
#     print(subject.ljust(8),str(score).rjust(4),sep=":") #서브젝트는 8공간할당하고 왼쪽정렬, 스코어는 4공간할당하고 오른쪽 정렬

#은행 대기순번표
 
# for num in range(1,21):
#     print("대기번호 : "+str(num))

# for num in range(1,21):
#     print("대기번호 : "+str(num).zfill(3)) #3만큼의 공간을 할당하고 빈공간에 0채우기

answer=input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 "+answer+"입니다.")