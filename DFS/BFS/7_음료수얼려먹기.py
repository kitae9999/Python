n=int(input(" "))
m=int(input(" "))
big_mat=[]
for i in range(0,n):
    small_mat=[]
    for j in range(0,m):
        small_mat.append(input())
    big_mat.append(small_mat)
    print("다음줄입력")
    #이렇게 코딩하면 small_mat의 주소와 big_mat[0]의 주소가 같아도 다음 for문이 시작되면서 새로운 주소의 small_mat이 생기므로 big_mat[0]의 값에는 문제가 없다
 
#좌상단쪽에 있는 0노드부터 시작해서 상하좌우 방문후에 방문한 노드는 방문처리하고 더이상 방문할 노드가 없는경우 count +1
visited=[]
for i in range(0,n):
    small_mat=[]
    for j in range(0,m):
        small_mat.append(False)
    visited.append(small_mat)
print(visited)

# n=int(input(" "))
# m=int(input(" "))
# big_mat=[]
# small_mat=[]
# for i in range(0,n):
#     for j in range(0,m):
#         small_mat.append(input())
#     print(small_mat)
#     big_mat.append(small_mat)
#     print(big_mat)
#     print("다음줄입력")
#     small_mat.clear()
#     print(big_mat)

# print(big_mat) #small_mat의 주소와 big_mat[0]의 주소는 같은데 small_mat을 clear해버리면 big_mat까지날아가버림