class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n= len(heights)
        i , j = 0, n-1
        max_val = -1
        cur = -1
        while i < j:
            cur  = min(heights[i], heights[j]) * (j-i)
            max_val = max(cur, max_val)
            if heights[i]>=heights[j]:
                j = j - 1
            else:
                i = i + 1
        return max_val