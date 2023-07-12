#킹, 퀸, 룩, 비숍, 나이트, 폰
#https://www.acmicpc.net/problem/3003
nums = list(map(int,input().split()))
pieces = [1,1,2,2,2,8]
for i in range(len(nums)):
	print(pieces[i]-nums[i],end=' ')
