class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        ordered_position = [(p,s) for p,s in zip(position, speed)]
        ordered_position.sort(reverse=True)
        for p, s in ordered_position:
            if not stack or (target-p)/s > stack[-1]:
                stack.append((target-p)/s)
        print(stack)
        return len(stack)