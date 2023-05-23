#두 배열의 원소 교체
"""
input:
5 3
1 2 5 4 3
5 5 6 6 5
output:
26
"""
N,K=map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
for i in range(K):
    if min(A)<max(B):
        A.append(max(B))
        A=A[1:len(A)]
        B=B[:len(B)-1]

print(sum(A))
