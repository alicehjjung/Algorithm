#나이순 정렬
#https://www.acmicpc.net/problem/10814
N = int(input())
names = []
for i in range(0,N):
	a,b=input().split()
	names.append((int(a),b))

names = sorted(names,key=lambda x: x[0])

for i in names:
	print(i[0],i[1])
