class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        i,j = 0,0
        minp = float('inf')
        maxv = -1
        for val in prices:
            minp = min(minp, val)
            maxv = max(maxv, val-minp)
        return maxv
        