class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = -1
        maxval = nums[0]
        for val in nums:
            if cur < 0:
                cur = 0
            cur += val
            maxval = max(maxval , cur)
        
        return maxval