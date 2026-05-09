class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        s1 = [0] * 26
        s2 = [0] * 26

        for i in range(len(s)):
            key1 = ord(s[i]) - ord('a')
            key2 = ord(t[i]) - ord('a')
            s1[key1] += 1
            s2[key2] += 1

        
        return s1 == s2