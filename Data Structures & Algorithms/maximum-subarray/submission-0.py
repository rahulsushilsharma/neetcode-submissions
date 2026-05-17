class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, msum = 0, nums[0]

        for val in nums:
            if cur < 0:
                cur = 0
            cur += val
            msum = max(cur, msum)
        return msum