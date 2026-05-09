class Solution:
    def isAnagram(self,s1:str, s2:str):
        if len(s1) != len(s2):
            return False
        
        arr1 = [0] * 26
        arr2 = [0] * 26

        for i in range(len(s1)):
            key1 = ord(s1[i]) - ord('a')
            key2 = ord(s2[i]) - ord('a')
            arr1[key1] += 1
            arr2[key2] += 1
        return arr1 == arr2

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        n = len(strs)
        seen = [0] * n
        for i in range(n):
            temp = []
            temp.append(strs[i])
            if seen[i] == 1:
                continue
            
            for j in range(i+1 , n):
                if self.isAnagram(strs[i], strs[j]):
                    temp.append(strs[j])
                    seen[j] = 1

            res.append(temp)
        return res