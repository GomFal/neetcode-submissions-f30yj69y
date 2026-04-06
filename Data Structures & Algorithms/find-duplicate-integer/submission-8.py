class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       # Floyds Haire and Tortoise Algorithm

        sp, fp = 0, 0
        while True:
            sp = nums[sp]
            fp = nums[nums[fp]]
            if sp == fp:
                break
        
        # Our sp is at the same point as our fp, we can now calculate the start of the cycle.
        sp2 = 0
        while True:
            sp2 = nums[sp2]
            sp = nums[sp]
            if sp == sp2:
                return sp


        


