class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        ordered_position = [(p,s) for p,s in zip(position, speed)]
        ordered_position.sort(reverse=True)
        for p, s in ordered_position:
            time = (target-p)/s
            if not stack or time > stack[-1]:
                stack.append(time)
        print(stack)
        return len(stack)