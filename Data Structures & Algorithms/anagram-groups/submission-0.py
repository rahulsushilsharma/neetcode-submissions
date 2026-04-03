class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}

        for i in range(len(strs)):

            cur = "".join(sorted(strs[i]))
            if cur in cache:
                cache[cur].append(strs[i])
            else :
                cache[cur] = [strs[i]]

        res = []
        for val in cache:
            res.append(cache[val])

        return res