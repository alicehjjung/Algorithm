#1이 될 때까지
"""
input:
17 4
output:
3

input:
25 5
output:
2
"""
#input
N, K = map(int,input().split())

count=0 #count

while True:
    #Check if N is evenly divisible by K
    if N%K==0: #If N is evenly divisble by K, divide N by K
        N//=K 
    else: #else subtract 1 from N
        N-=1
    
    count+=1 #add 1 on count
    
    if N==1: #If N is 1, break a while loop
        break

print(count)