class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # + - * /
        stack = []
        for token in tokens:
            if token == "+":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(int(val1) + int(val2))

            elif token == "-":
                val2, val1 = stack.pop(), stack.pop()
                stack.append(int(val1) - int(val2))

            elif token == "*":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(int(val1) * int(val2))

            elif token == "/":
                val2, val1 = stack.pop(), stack.pop()
                stack.append(int(int(val1) / int(val2)))

            else:
                stack.append(int(token))
        
        return stack[0]