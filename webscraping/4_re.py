import re
#abcd,book,desk
#ca?e

p=re.compile("ca.e") 
# . : 하나의 문자를 의미 > care, cafe, case | caffe
# ^ (^de): 문자열의 시작 > desk, destiny | fade
# $ (se$): 문자열의 끝 > case, base | face

def print_match(m):
    if m:
        print(m.group())#매치되지 않으면 에러가 발생 
    else:
        print("매칭되지않음")
        
# m=p.match("case") #주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

m=p.search("good care") #search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)