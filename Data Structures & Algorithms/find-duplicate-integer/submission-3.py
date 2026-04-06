class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Use Floyds Hair and Tortoise algorithm:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Once we've met both pointers, we stablish Slow pointer 2, 
        # and meet it with Slow pointer 1 to find the solution
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

