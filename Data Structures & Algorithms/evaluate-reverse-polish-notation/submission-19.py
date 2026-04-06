class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # + - * /
        stack = []
        for t in tokens:
            if t == "+":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(val1+val2) 

            elif t == "*":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(val1 * val2)

            elif t == "-":
                val2, val1 = stack.pop(), stack.pop()
                stack.append(val1 - val2)

            elif t == "/":
                val2, val1 = stack.pop(), stack.pop()
                stack.append(int(val1/val2))
                
            else:
                stack.append(int(t))
        return stack[0]
