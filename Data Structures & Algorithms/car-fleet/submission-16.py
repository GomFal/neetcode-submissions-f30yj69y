class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = [(p, s) for p, s in zip(position, speed)]
        sorted_cars.sort(key=lambda x: x[0],reverse=True)

        stack = []
        for p, s in sorted_cars:
            time = (target-p)/s
            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)



            
