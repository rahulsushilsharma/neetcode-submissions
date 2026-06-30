class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has = {}
        for num in nums:
            if num in has:
                has[num] += 1
            else:
                has[num] = 1
        
        buc = [[] for _ in range(len(nums) + 1)] 

        for key, val in has.items():
            buc[val].append(key)

        res = []
   
        for b in buc[::-1]:
            for val in b:
                res.append(val)
                if len(res) == k:
                    return res
        return res