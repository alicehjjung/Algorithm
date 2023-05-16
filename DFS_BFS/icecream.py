#음료수 얼려 먹기
"""
input:
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
output:
8
"""
#input
N,M = map(int,input().split())
graph=[]
for i in range(0,N):
    graph.append(list(map(int,input())))
count=0

def DFS(i,j):
    #if the coordinate is out of bounds, return false
    if i<0 or i>=N or j<0 or j>=M:
        return False
    #if the coordinate is not marked as passed, move and then return True
    if graph[i][j]==0:
        graph[i][j]=2 #mark it as passed
        DFS(i-1,j)
        DFS(i+1,j)
        DFS(i,j-1)
        DFS(i,j+1)
        return True
    #if the coordinate is marked as passed or blocked, return false
    return False

for i in range(0,N):
    for j in range(0,M):
        if DFS(i,j)==True:
            count+=1

print(count)