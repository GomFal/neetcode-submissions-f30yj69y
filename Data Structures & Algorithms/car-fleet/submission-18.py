class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        result = [] # In this array we will store the amount of hours cars take to reach the target.
        for p, s in pairs:
            time = (target-p)/s
            if not result:
                result.append(time)
            elif result and result[-1] < time:
                result.append(time)


        return len(result)



            
