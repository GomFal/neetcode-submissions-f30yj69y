class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedCars = [i for i in range(len(position))] 
        sortedCars.sort(reverse=True, key= lambda x: position[x])
        stack = []
        for i in sortedCars:
            time = (target-position[i])/speed[i]
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
        
        return len(stack)
