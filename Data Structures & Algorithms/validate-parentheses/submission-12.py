class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {'}':'{', ')':'(', ']':'['}
        stack = []
        for c in s:
            if c in lookup:
                if stack and lookup[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return False if stack else True
        