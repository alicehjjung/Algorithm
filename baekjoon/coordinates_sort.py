#좌표 정렬하기
#https://www.acmicpc.net/problem/11650
N = int(input())
coordinates=[]
for i in range(0,N):
    tmp1,tmp2=map(int,input().split())
    coordinates.append((tmp1,tmp2))
    
coordinates.sort(key=lambda x:(x[0],x[1]))

for i in range(0,N):
    print(coordinates[i][0],coordinates[i][1])
