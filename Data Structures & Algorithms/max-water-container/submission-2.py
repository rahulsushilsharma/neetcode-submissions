class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_val = -1
        cur = -1
        n  = len(heights)
        for i in range(n):
            for j in range(i+1 , n):
                longest = min(heights[i], heights[j])
                cur = longest * (j-i)
                max_val = max(cur, max_val)
        
        return max_val