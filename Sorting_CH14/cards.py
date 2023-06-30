"""
input:
3
10
20
40
output:
100
"""
N = int(input())
cards=[]
for i in range(0,N):
    cards.append(int(input()))
cards.sort(reverse=True)

for i in range(len(cards)-2,-1,-1):
    cards[i]=cards[i]+cards[i+1]

print(sum(cards[:-1]))
