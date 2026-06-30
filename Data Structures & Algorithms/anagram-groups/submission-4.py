class Solution:
    def ana_hash(self, s: str)->Tuple[int]:
        freq = [0]*26
        for val in s:
            index = ord(val) - ord("a")
            freq[index] += 1
        return tuple(freq)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        has = {}

        for s in strs:
            index = self.ana_hash(s)
            if index in has:
                has[index].append(s)
            else:
                has[index] = [s]
        res = []
        for _, val in has.items():
            res.append(val)
        return res
