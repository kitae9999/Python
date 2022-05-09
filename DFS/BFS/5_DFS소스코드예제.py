def dfs(graph,v,visited):

    visited[v]=True
    print(v,end="")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]

]

visited=[False] * 9 #노드 방문 정보를 알려주는 리스트 작성 ex)[False,False,False,False,False,False,False,False,False]

dfs(graph,1,visited)