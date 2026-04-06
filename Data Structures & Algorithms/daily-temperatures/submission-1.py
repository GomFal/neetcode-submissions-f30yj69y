class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # : Store pair values (i,temperature)
        result = [0]*len(temperatures)
        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][1]:
                index, temperature = stack.pop()
                result[index] = i - index
            stack.append((i,n))
        return result

