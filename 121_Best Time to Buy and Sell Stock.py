class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far=prices[0]
        maxprofit=0
        for i in prices:
            min_so_far=min(min_so_far,i)
            maxprofit=max(maxprofit,i-min_so_far)
        return maxprofit
