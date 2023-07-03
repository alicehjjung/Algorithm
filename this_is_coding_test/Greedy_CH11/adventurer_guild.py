#모험가 길드
"""
input : 
5
2 3 1 2 2
output : 
2
"""
#input
N = int(input())
rate = list(map(int,input().split()))

rate.sort()
count,num=0,0

for i in rate:
    num+=1
    #현재 그룹 인원수가 공포도보다 같거나 크다면 새로운 그룹 결성
    if num>=i: 
        count+=1
        num=0

print(count)
