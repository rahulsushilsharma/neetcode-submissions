class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = -1
        n = len(prices)

        for i in range( n):
            for j in range(i,n):
                max_p = max(max_p , prices[j]-prices[i])
        return max_p