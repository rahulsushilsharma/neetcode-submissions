class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}


        for val in strs:
            key = tuple(sorted(val))
            if key in seen:
                seen[key].append(val)
            else:
                seen[key] = [val]
        
        res  = []
        for key in seen:
            res.append(seen[key])

        return res