#전보
"""
input:
3 2 1
1 2 4
1 3 2
output:
2 4
"""
import heapq
import sys
input = sys.stdin.readline
INF=int(1e9)

n,m,c=map(int,input().split())

graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    i, j, k = map(int,input().split())
    graph[i].append((j,k))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)

count,time=0,0
for i in range(1, n+1):
    if i!=c:
      if distance[i]!=0 and distance[i]!=INF:
          count+=1
          time=max(time,distance[i])

print(count, time)
