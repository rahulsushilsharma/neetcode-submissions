class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = {i for i in nums}

        max_val = 0
        for val in nums:
            if val-1 in num_set:
                continue
            
            cur = 0
            cur_val = val
            while cur_val in num_set:
                cur += 1
                max_val = max(max_val, cur)
                cur_val += 1
        
        return max_val