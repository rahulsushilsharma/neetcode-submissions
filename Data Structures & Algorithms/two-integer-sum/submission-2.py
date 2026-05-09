class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,val in enumerate(nums):
            cur = target - val
            if cur in seen:
                return [seen[cur], i]
            else:
                seen[val] = i
        return [0,0]