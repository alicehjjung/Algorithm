class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,1
        
        for i in range(2, n+1):
            tmp=b
            b=a+b
            a=tmp

        return b
