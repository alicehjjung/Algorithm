#커트라인, https://www.acmicpc.net/problem/25305

#input
N,k=map(int,input().split())
nums=list(map(int,input().split()))

#sort
nums.sort(reverse=True)
print(nums[k-1])
