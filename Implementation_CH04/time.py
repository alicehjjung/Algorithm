#시각
"""
If there is at least one 3, add 1 to count
input:
5
output:
11475
"""
#input
N = int(input())
count=0 

#loops
for hour in range(0,N+1):
    for min in range(0,60):
        for sec in range(0,60):
            #If there is 3 in the string, add 1 to the count
            if '3' in str(hour)+str(min)+str(sec):
                count+=1
print(count)