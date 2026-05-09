class Solution:
    def topKFrequent(self, nums: List[int], k_: int) -> List[int]:
        n = len(nums)
        bucket = [[] for i in range(n+1)] 
        res = []
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1

            else:
                freq[i] = 1
        for k,val in freq.items():
            # print(k,val)
            bucket[val].append(k)
        cnt = k_
        
        for i in range(n,-1,-1 ):
            if cnt == 0 :
                break
            for buck in bucket[i]:
                res.append(buck)
                cnt -= 1

        return res
