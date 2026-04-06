class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while numbers[l] + numbers[r] != target:
            while numbers[l] + numbers[r] > target:
                print("right before change: ",numbers[r])
                r -= 1
                print("right after change: ", numbers[r])
            while numbers[l] + numbers[r] < target:
                print("left before change: ", numbers[l])
                l += 1
                print("left after change: ", numbers[l])
            print(numbers[l], numbers[r])
        return [l+1,r+1]