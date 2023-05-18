#위에서 아래로
"""
input:
3
15
27
12
output:
27 15 12
"""
#input
N = int(input())
numbers=[]
for i in range(0,N):
    numbers.append(int(input()))

#bubble sort, descending order
for i in range(0,N):
    tmp=numbers[i]
    for j in range(i+1,N):
        if tmp<numbers[j]:
            numbers[i],numbers[j]=numbers[j],tmp

#print output
for i in range(0,len(numbers)):
    print(numbers[i],end=' ')