class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        has = {}
        for i, num in enumerate(nums):
            has[num] = i
        
        max_len = 1

        for num in nums:
            prev = num - 1
            if prev in has:
                continue
            
            next_val = num + 1
            cur = 1
            while next_val in has:
                next_val += 1
                cur += 1
                max_len = max(max_len , cur)

        
        return max_len