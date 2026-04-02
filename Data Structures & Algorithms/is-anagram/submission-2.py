class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq1  , freq2 = {},{}
        for i in range(len(s)):
            if s[i] in freq1:
                freq1[s[i]] += 1
            else :
                freq1[s[i]] = 1
            if t[i] in freq2:
                freq2[t[i]] += 1
            else :
                freq2[t[i]] = 1
        
        for key,val in freq1.items():
            if key not in freq2 or freq2[key] != val:
                return False

        return True
        