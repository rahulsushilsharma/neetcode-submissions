class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has={}
        for num in nums: 
            if num in has:
                return True
            else:
                has[num] = 1
        
        return False