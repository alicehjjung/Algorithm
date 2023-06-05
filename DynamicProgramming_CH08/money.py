#효율적인 화폐 구성
"""
input:
2 15
2
3
output:
5
"""
#input
N,M=map(int,input().split())
money=[]
for i in range(N):
    money.append(int(input()))

dp=[0]+[10001]*M

for i in range(money[0],M+1):
    if i in money:
        dp[i]=1
    else: 
        for j in money:
            if i-j>=1:
                dp[i]=min(dp[i],dp[i-j]+1)

if dp[M]==10001:
    print(-1)
else:
    print(dp[M])