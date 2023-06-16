#문자열 뒤집기
"""
input:
0001100
output:
1
"""
#input
N=list(map(int,input()))
count1=1 if N[0]==0 else 0
count2=1 if N[0]==1 else 0

for i in range(1,len(N)):
    #change 0 to 1
    if N[i]==0: 
        #Increment count1 if there is a change in the sequence
        if N[i]!=N[i-1]: 
            count1+=1
    #change 1 to 0
    else: 
        #Increment count2 if there is a change in the sequence occurrence
        if N[i]!=N[i-1]:
            count2+=1

print(min(count1,count2))

