class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            cache[nums[i]] = i
        print(cache,nums)
        for i in range(len(nums)):
            if target - nums[i]  in cache and cache[target-nums[i]] != i:
                return [i,cache[target - nums[i]]]
        
        return [-1,-1]