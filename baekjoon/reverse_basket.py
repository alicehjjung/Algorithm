#바구니 뒤집기
#https://www.acmicpc.net/problem/10811
N, M = map(int,input().split())
nums = [i for i in range(1,N+1)]

for i in range(0,M):
	a, b = map(int,input().split())
	nums[a-1:b] = nums[a-1:b][::-1]

for i in nums:
    print(i,end=' ')
