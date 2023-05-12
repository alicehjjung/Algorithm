#왕실의 나이트
"""
input:
a1
output:
2
"""
#input
coordinate = input()
#convert alphabet to number
alphabet={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
x=alphabet[coordinate[0]]
y=int(coordinate[1])

count=0
directions=[(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
for d in directions:
    tmp1,tmp2=x+d[0],y+d[1]
    #If the coordinate is in boundaries, add 1 to count
    if tmp1>=1 and tmp1<=8 and tmp2>=1 and tmp2<=8:
        count+=1

print(count)