class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # + - * /

        stack = []

        for c in tokens:
            if c == "+":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(int(val1) + int(val2))

            elif c == "-":
                val2, val1 = stack.pop(), stack.pop()
                stack.append(int(val1) - int(val2))

            elif c == "*":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(int(val1) * int(val2))

            elif c == "/":
                val2, val1 = stack.pop(), stack.pop()
                stack.append(int(val1 / val2))

            else:
                stack.append(int(c))
        return stack[0]
            