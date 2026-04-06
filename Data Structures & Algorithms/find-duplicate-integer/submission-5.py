class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # We detect that its a linked list
        # Now, we need to detect if there is a cycle. A cycle is detected when, using the Floyds Hair and Tortoise
        # Algorithm, we find that the slow and fast pointers arrive to the same point. 
        # Once we arrive to the same point, we have an equal distance from the start of the linked list to the
        # Start of the cycle, so we stablish one pointer at the start, another at where our sp and fp met,
        # and when they meet, we know that this is the start of the cycle, and, the number which is being repeated.

        # F h and T algo
        sp, fp = 0, 0
        while True:
            sp = nums[sp]
            fp = nums[nums[fp]]
            if sp == fp:
                break
        print(sp)
        # We have got the slow pointer where it meets the fp. Now, we find the start of the cycle
        # We start a slow pointer on the start of the linked list
        sp2 = 0
        while True:
            sp = nums[sp]
            sp2 = nums[sp2]
            if sp == sp2:
                return sp


