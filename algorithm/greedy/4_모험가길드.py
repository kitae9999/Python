explorer_num=int(input("모험가는 총 몇명입니까? "))
infor=list()
count=0
group_count=0
for i in range(1,explorer_num+1):
    infor.append(input())

#공포도가 x인 모험가는 x명으로 이루어진 그룹속에 있어야함
#여행을 떠널 수 있는 그룹 수의 최댓값 구하기 
#몇명의 모험가는 마을에 그대로 남아있어도된다, 모든 모험가를 특정한 그룹에 넣을 필요 없음

#solution 
#공포도가 낮은 모험가부터 그룹처리함
#공포도가 1이 아닐시에는 공포심이 같은 모험가들 끼리 그룹처리해야함

# 1 1 2 2 3 4 4 6
infor.sort() #공포도 순으로 정렬함
print(infor)
#같은 공포도를 가진 모험가가없으면 더 큰 공포를 가진 모험가의 동료가되어야함

max_num=int(max(infor))
print(max_num)
for i in range(1,max_num+1):
    for j in range(0,len(infor)): 
        if int(infor[j])==i:  #범한 실수->리스트의 요소를 정수변환해주지않았음
            count+=1
        if j==len(infor)-1:
            if count%i==0: #나머지가 0이면 배수
                group_count+=(count/i)
            count=0 

     

print(group_count)

