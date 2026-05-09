class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            cur = 1
            for j in range(n):
                if j == i:
                    continue
                else:
                    cur *= nums[j]
            res.append(cur)
        return res