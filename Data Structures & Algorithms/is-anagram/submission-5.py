class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26
        for val in s:
            idx = ord(val) - ord('a')
            freq[idx] += 1
        
        for val in t:
            idx = ord(val) - ord('a')
            freq[idx] -= 1
        
        for val in freq:
            if val != 0:
                return False
        
        return True