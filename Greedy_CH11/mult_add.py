#곱하기 혹은 더하기
"""
input:
02984
output:
567
"""
#input
N=list(map(int,input()))

#sort
N.sort(reverse=True)
result=N[0]

for i in N[1:]:
    #If i is not 0 or 1, multiply result by i
    if i!=0 and i!=1:
        result*=i
    else:
        result+=i

print(result)
