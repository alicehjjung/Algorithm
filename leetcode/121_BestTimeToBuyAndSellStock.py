class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num, profit = prices[0],0

        for i in prices[1:]:
            if i-num>profit:
                profit = i-num
            if i<num:
                num=i

        return profit
