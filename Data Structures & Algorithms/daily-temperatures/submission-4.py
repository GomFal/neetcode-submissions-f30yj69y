class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # We use a stack to store the temperatures in descending order, popping them when a higher temperature appears
        stack = []  # (index, temp)
        res = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                index, temp = stack.pop()
                res[index] = i-index
            stack.append((i, t))
        
        return res






















