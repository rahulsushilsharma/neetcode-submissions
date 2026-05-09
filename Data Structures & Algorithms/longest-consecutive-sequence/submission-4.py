class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        mx = 0
        for val in nums:
            if val-1 in ns:
                continue
            cur = 0
            cv = val
            while cv in ns:
                cur += 1
                mx = max(mx, cur)
                cv += 1
        
        return mx