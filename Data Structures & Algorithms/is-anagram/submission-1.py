class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sort_s = [0]*27
        sort_t = [0]*27
        for i in range(len(s)):
            sort_t[ord(s[i])-ord('a')] += 1
            sort_s[ord(t[i])-ord('a')] += 1

        
        for i in range(27):
            if sort_t[i] != sort_s[i]:
                return False
        return True