N=int(input())
P=list(map(int,input().split()))

for i in range(0,N):
    for j in range(0,i):
        P[i]=max(P[i],P[i-j]+P[j])

print(P[N-1])
