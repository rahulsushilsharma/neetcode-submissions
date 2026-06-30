class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}

        for i, val in enumerate(nums):
            find = target - val

            if find in has:
                return [has[find], i]
            else:
                has[val] = i
        return [0,0]