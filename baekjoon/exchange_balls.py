#공 바꾸기
#https://www.acmicpc.net/problem/10813
N, M = map(int,input().split())
nums = [i for i in range(0,N+1)]
for i in range(0,M):
	a,b=map(int,input().split())
	nums[a],nums[b] = nums[b],nums[a]

for i in range(1,N+1):
    print(nums[i],end=" ")
