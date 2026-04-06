class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedCars = [i for i in range(len(position))] 
        sortedCars.sort(reverse=True, key= lambda x: position[x])
        stack = []
        time = (target-position[sortedCars[0]])/speed[sortedCars[0]]
        stack.append(time)
        print(sortedCars)
        print(stack)
        for i in sortedCars[1::]:
            print(i)
            time = (target-position[i])/speed[i]
            print(time)
            if time > stack[-1]:
                stack.append(time)
        print(stack)
        return len(stack)
