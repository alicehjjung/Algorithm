#대칭 차집합
#https://www.acmicpc.net/problem/1269
A,B=map(int,input().split())
num_A=set(list(input().split()))
num_B=set(list(input().split()))

newA=num_A-num_B
newB=num_B-num_A
print(len(newA)+len(newB))
