class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('inf')
        maxv = -1
        for val in prices:
            minp = min(minp, val)
            maxv = max(maxv, val-minp)
        return maxv
        