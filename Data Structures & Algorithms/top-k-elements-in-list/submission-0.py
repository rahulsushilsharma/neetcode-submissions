class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = {}
        for val in nums:
            if val in cache:
                cache[val] += 1
            else:
                cache[val] = 1
        
        res = []
        for i in range(k):
            cur_max = -1
            cur_key = -1
            for val in cache:
                if cache[val] > cur_max:
                    cur_max = cache[val]
                    cur_key = val
            
            res.append(cur_key)
            cache[cur_key] = -1
        return res