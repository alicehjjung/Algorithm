#안테나
"""
input:
4
5 1 7 9
output:
5
"""
N = int(input())
location = list(map(int,input().split()))
location.sort()

print(location[(N-1)//2])
