class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_close = {"}":"{", "]":"[", ")":"("}
        for c in s:
            if stack and c in open_to_close and open_to_close[c] == stack[-1]:
                stack.pop()
            elif stack and c in open_to_close and open_to_close[c] != stack[-1]:
                return False
            else:
                stack.append(c)

        return True if len(stack) == 0 else False
                