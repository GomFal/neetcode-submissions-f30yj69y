class Solution:
    def isValid(self, s: str) -> bool:
        is_closed = {'}':'{', ')':'(', ']':'['}
        stack = []
        for c in s:
            if c not in is_closed:
                stack.append(c)
            else:
                if stack and stack[-1] == is_closed[c]:
                    stack.pop()
                else:
                    return False

        return not stack