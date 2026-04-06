class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        ordered_cars = [(p,s) for p,s in zip(position, speed)]
        ordered_cars.sort(reverse=True)
        for p, s in ordered_cars:
            time = (target-p)/s
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)