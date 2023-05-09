#예제 4-1 상하좌우
"""
input:
5
R R R U D D
output:
3 4
"""
def check(a,b,x,y):
    #check boundaries
    if x<1 or x>N:
        x-=a
    if y<1 or y>N:
        y-=b
    return x,y

#input
N=int(input())
directions=list(input().split())
x,y=1,1 #initial coordinate

for direction in directions:
    if direction=='L':
        y-=1 
        x,y=check(0,-1,x,y)
    elif direction=='R':
        y+=1
        x,y=check(0,1,x,y)
    elif direction=='U':
        x-=1
        x,y=check(-1,0,x,y)
    elif direction=='D':
        x+=1
        x,y=check(1,0,x,y)

print(x,y)