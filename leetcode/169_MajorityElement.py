class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num, maj = 0, 0

        for i in nums:
            if num != i:
                maj -= 1
                if maj<0:
                    num=i
                    maj=0
            else:
                maj +=1

        return num

        
