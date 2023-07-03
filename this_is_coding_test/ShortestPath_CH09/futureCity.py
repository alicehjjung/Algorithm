#미래 도시
"""
input:
4 2
1 3
2 4
3 4
output:
-1
"""
INF=int(1e9)

#input
N,M=map(int,input().split())
graph = [[INF]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i==j:
            graph[i][j]=0

for a in range(M):
    i,j=map(int,input().split())
    graph[i-1][j-1]=1
    graph[j-1][i-1]=1

X,K=map(int,input().split())

#Floyd-Warsahll Algorithm
for i in range(N):
    for j in range(N):
        for k in range(N):
            graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k])

distance=graph[1][K-1]+graph[K-1][X-1]

if distance>=INF:
    print(-1)
else:
    print(distance)
