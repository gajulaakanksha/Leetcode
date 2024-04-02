class Solution:
    def __init__(self,prices):
        self.prices=prices
    def maxProfit(self, prices:[int]) -> int:
        profit = 0
        small = prices[0]
        for i in prices[1:]:
            if i > small:
                profit = max(profit, i - small)
            else:
                small = i
        return profit   
prices=[7,1,5,3,6,4]
solution=Solution(prices)
result=solution.maxProfit(prices)
print(result)
         
        