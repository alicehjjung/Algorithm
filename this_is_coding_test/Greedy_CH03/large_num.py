#큰 수의 법칙
"""
input :
5 8 3
2 4 5 4 6
output :
46

input :
5 7 2
3 4 3 4 3
output :
28
"""
#inputs
N, M, K = map(int,input().split())
nums = list(map(int,input().split()))

nums.sort(reverse=True) #sorting
largest=nums[0] #the largest number
largest2=nums[1] #the second largest number
total=0 #total

while True:
    #if M is less than K, add the largest number M times
    #else, M is equal or greater than K, add the largest number K times
    if M<K:
        total+=largest*M
        M=0
    else:
        total+=largest*K
        M-=K

    #if M is equal to 0, stop the iteration
    if M==0:
        break
    
    #add the second largest number to total
    total+=largest2
    M-=1

print(total)