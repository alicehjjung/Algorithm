#개미전사
"""
input:
4
1 3 1 5
output:
8
"""
#input
N=int(input())
food=list(map(int,input().split()))

#dp
dp=[0]*N
dp[0],dp[1]=food[0],max(food[0],food[1])

for i in range(2,N):
    dp[i]=max(dp[i-1],food[i]+dp[i-2])

print(dp[N-1])