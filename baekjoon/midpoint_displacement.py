#중앙 이동 알고리즘, midpoint displacement algorithm
#https://www.acmicpc.net/problem/2903
N=int(input())

add=0
for i in range(0,N):
    add+=2**i
    
print((2+add)**2)
