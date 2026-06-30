class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = [0] * 26
        for i in range(len(s)):
            asc1 = ord(s[i])
            asc2 = ord(t[i])

            freq[asc1 - ord('a')] += 1
            freq[asc2 - ord('a')] -= 1
        
        for check in freq:
            if check != 0:
                return False
            
        return True