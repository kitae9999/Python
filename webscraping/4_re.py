import re
#abcd,book,desk
#ca?e

p=re.compile("ca.e") 
# . : 하나의 문자를 의미 > care, cafe, case | caffe
# ^ (^de): 문자열의 시작 > desk, destiny | fade
# $ (se$): 문자열의 끝 > case, base | face

m=p.match("case")
print(m.group) #매치되지 않으면 에러가 발생 zmn 

if m:
    print(m.group())
else:
    print("매칭되지않음")