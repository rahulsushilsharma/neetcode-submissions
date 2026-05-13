class Solution:
    def isValid(self, s: str) -> bool:
        key_map = {
            '{': "}",
            "(":")",
            "[":"]"
        }
        stack = []
        for val in s:
            if val in key_map:
                stack.append(key_map[val])
            else:

                if len(stack) == 0:
                    return False
                if stack[-1] == val:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0