class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {']':'[', '}':'{', ')':'('}
        stack = []

        for c in s:
            if stack and c in close_to_open and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                if not stack and c in close_to_open:
                    return False
                else:
                    stack.append(c)
        
        return True if not stack else False

                