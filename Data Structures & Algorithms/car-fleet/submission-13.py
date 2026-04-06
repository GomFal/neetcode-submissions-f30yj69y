class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = [(i, p) for i, p in enumerate(position)]
        sorted_cars.sort(key=lambda x: x[1], reverse=True)
        
        stack = []
        print(sorted_cars)
        for i, p in sorted_cars:
            time = (target-p)/speed[i]
            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)
            
