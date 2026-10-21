class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for n in nums:
            if n in mp:
                return True
            mp[n] = 1
        return False
        
        # seen = set()
        # for n in nums:
        #     if n in seen:
        #         return True
        #     seen.add(n)
        # return False