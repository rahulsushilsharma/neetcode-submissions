class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_str = "".join(char for char in s if char.isalnum())
        n = len(clean_str)
        i , j = 0, n-1
        while i < j:
            print(clean_str[i], clean_str[j])
            if clean_str[i].lower() != clean_str[j].lower():
                return False
            
            i += 1
            j -= 1
        return True

