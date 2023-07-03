#대표값2
nums=[]
sums=0
for i in range(0,5):
    tmp=int(input())
    nums.append(tmp)
    sums+=tmp
        
nums.sort()
print(sums//5)
print(nums[2])
