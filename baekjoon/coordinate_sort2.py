N=int(input())
x=[]
for i in range(N):
    a,b=map(int,input().split())
    x.append([a,b])
        
x.sort(key = lambda x: (x[1], x[0]))

for i in x:
    print(i[0],i[1])
