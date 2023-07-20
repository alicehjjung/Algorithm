#개수 세기
#https://www.acmicpc.net/problem/10807
N=int(input())
nums=list(map(int,input().split()))
v=int(input())
count=0

for i in range(0,N):
	if nums[i]==v:
		count+=1

print(count)
