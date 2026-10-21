class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res =[]
        prod = 1
        zero_cnt = 0
        for n in nums:
            if n == 0:
                zero_cnt += 1
            else:
                prod *= n
        
        if zero_cnt > 1:
            return [0]*len(nums)
        
        res = [0]*len(nums)

        for i, n in enumerate(nums):
            if zero_cnt: res[i] = 0 if n else prod
            else: res[i] = prod//n
        return res