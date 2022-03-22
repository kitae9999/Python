python="Python is Amazing"
print(len(python)) #문자열 길이 반환
print(python.replace("Python","C++")) #문자열 찾아서 바꾸기

index =python.index("n") #문자열에서 n의 첫번째 위치 반환
print(index)
index=python.index("n",index+1)

print(python.find("n")) #내가 원하는 문자의 위치반환, 문자열에 없을시에는 -1 반환

print(python.count("n")) #원하는 문자가 문자열에서 몇번나왔는지를 반환

print("나는 {}살 입니다. ".format(20))
print("나는 {age}색과 {color}색을 좋아해요.".format("파란","빨간"))
print("나는 {age}살이며,{color}색을 좋아해요".format(age=20,color="빨간"))

age=20
color="빨간"
print(f"나는 {age}살이먀, {color}색을 좋아해요.")





