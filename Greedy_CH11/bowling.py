#볼링공 고르기
"""
input:
5 3
1 3 2 3 2
output:
8
"""
N,M=map(int,input().split())
nums=list(map(int,input().split()))
count=0

for i in range(0,N-1):
    for j in nums[i+1:N]:
        if nums[i]!=j:
            count+=1

print(count)
