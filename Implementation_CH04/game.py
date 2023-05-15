#게임 개발
"""
input:
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
output:
3
"""
#input
N,M=map(int,input().split())
x,y,d=map(int,input().split())

maps=[]
for i in range(0,N):
    maps.append(list(map(int,input().split())))

maps[x][y]=2 #mark it as passed(2)

move=[(-1,0),(0,1),(1,0),(0,-1)]
direct={0:3,1:0,2:1,3:2} #key:current direction, value:direction when it turn left
count=1
turn=0

while True:
    d=direct[d] #turn left
    tmpX,tmpY = x+move[d][0], y+move[d][1] 

    if maps[tmpX][tmpY]==0:
        maps[tmpX][tmpY]=2 #mark it as passed(2)
        count+=1 #add count when movement is available
        turn=0 #initialize turn
        x,y=tmpX,tmpY #move
        continue
    else:
        turn+=1

    if turn==4:
        #move backward
        x-=move[d][0]
        y-=move[d][1]
        if maps[x][y]==1:
            break
        turn=0 #initialize turn

print(count)