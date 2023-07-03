"""
input:
5 6
101010
111111
000001
111111
111111
output:
10
"""
from collections import deque
#input
N, M = map(int,input().split())
graph=[]
for i in range(0,N):
    graph.append(list(map(int,input())))
direct=[(-1,0),(1,0),(0,-1),(0,1)]

#BFS
def BFS(graph,x,y):
    queue = deque([(x,y)])
    while queue:
        coor=queue.popleft()
        #move 
        for i in direct:
            tmpX,tmpY=coor[0]+i[0],coor[1]+i[1]
            #if the coordinate is in bounds and not marked as passed
            if 0<=tmpX and tmpX<N and 0<=tmpY and tmpY<M and graph[tmpX][tmpY]==1:
                #add the coordinate in the queue
                queue.append((coor[0]+i[0],coor[1]+i[1]))
                #mark the coordinate as passed with the number of coordinates it has passed
                graph[tmpX][tmpY]=graph[coor[0]][coor[1]]+1
    return graph[N-1][M-1]

print(BFS(graph,0,0))
