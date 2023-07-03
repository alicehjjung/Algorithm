#숫자카드 게임
"""
input:
3 3
3 1 2
4 1 4
2 2 2
output:
2

input:
2 4
7 3 1 8
3 3 3 4
output:
3
"""
#inputs
N,M = map(int,input().split())
cards = [list(map(int,input().split())) for _ in range(N)]

#An array that stores the minimum number of each row
arr = []
for i in cards:
    arr.append(min(i))

#Print the maximum number among the minimum numbers of each row
print(max(arr))