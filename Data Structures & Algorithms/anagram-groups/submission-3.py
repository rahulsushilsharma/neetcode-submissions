class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}


        for val in strs:
            temp = [0] * 26
            for c in val:
                k = ord(c) - ord('a')
                temp[k] += 1

            key = tuple(temp)
            if key in seen:
                seen[key].append(val)
            else:
                seen[key] = [val]
        
        res  = []
        for key in seen:
            res.append(seen[key])

        return res