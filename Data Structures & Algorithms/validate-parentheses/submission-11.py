class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {'}':'{', ')':'(', ']':'['}
        stack = []
        for c in s:
            if stack:
                if c in lookup and lookup[c] == stack[-1]:
                    stack.pop()
                elif c in lookup and lookup[c] != stack[-1]:
                    return False
                else:
                    stack.append(c)
            else:
                stack.append(c)

        return False if len(stack) != 0 else True
        