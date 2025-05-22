class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for i in nums:
            count[i] = 1+count.get(i,0)
            
            if count[i]>=2:
                return True
        
        return False
