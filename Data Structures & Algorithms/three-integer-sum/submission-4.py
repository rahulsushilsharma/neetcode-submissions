class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [ ]
        nums = sorted(nums)
        n = len(nums)
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left  = i + 1
            right = n - 1

            while left < right:

                cur = nums[i] + nums[left] + nums[right]

                if cur > 0:
                    right -= 1
                elif cur < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left+1] == nums[left]:
                        
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1


                
        return res
