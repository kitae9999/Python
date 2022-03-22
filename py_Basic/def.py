# def open_account():
#     print("새로운 계좌가 생성되었습니다. ")

# def deposit(balance,money): #입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
#     return balance+money

# def withdraw(balance,money): #출금
#     if balance>money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
#         return balance-money
#     else:
#         print("츨금이 완료되지 않았습니다. 잔액은 {0} 원입니다".format(balance))
#         return balance
    
# def withdraw_night(balance,money):
#     commission=100
#     return commission,balance-money-commission #값 두개 반환

# balance =0
# balance =deposit(balance,1000)
# commission,balance=withdraw_night(balance,500)
# print("수수료 {0}원이며, 잔액은{1} 원입니다.".format(commission,balance))

# def profile(name,age,main_lang):
#     print("이름 : {0}\t 나이 : {1}\t주 사용 언어: {2}"\
#         .format(name,age,main_lang))

# profile("유재석",20,"파이썬")
# profile("김태호",25,"자바")

#같은 학교 같은 학년 같은 반 같은 수업인 경우
# def profile(name,age=17,main_lang="파이썬"): #기본값 설정
#     print("이름 : {0}\t 나이 : {1}\t주 사용 언어: {2}"\
#         .format(name,age,main_lang))

#가변인자
# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름 : {0}\t 나이 : {1}\t".format(name,age),end=" ") #end=" " 문장이 끝날때 줄바꿈하지않고 빈칸으로 이어짐
#     print(lang1,lang2,lang3,lang4,lang5)

# def profile(name,age,*language):
#     print("이름 : {0}\t 나이 : {1}\t".format(name,age),end=" ") #end=" " 문장이 끝날때 줄바꿈하지않고 빈칸으로 이어짐
#     for lang in language:
#         print(lang,end=" ")
#     print()

# profile("유재석",20,"python","java","c","c++","c#")
# profile("김태호",20,"python")  #서로 다른 개수의 값 전달가능




