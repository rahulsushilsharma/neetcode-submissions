class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            val = nums[i]
            hash[val] = i
        

        for i in range(len(nums)):
            val = nums[i]

            if target - val in hash and hash[target-val] != i:
                return [i,hash[target-val]]

        return [-1,-1]