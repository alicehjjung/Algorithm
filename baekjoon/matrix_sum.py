#행렬 덧셈
#https://www.acmicpc.net/problem/2738
N,M = map(int,input().split())
A,B=[],[]
for i in range(0,N):
	tmp=list(map(int,input().split()))
	A.append(tmp)

for i in range(0,N):
	tmp=list(map(int,input().split()))
	B.append(tmp)

for i in range(0,N):
	for j in range(0,M):
		print(A[i][j]+B[i][j],end=" ")
	print("")
