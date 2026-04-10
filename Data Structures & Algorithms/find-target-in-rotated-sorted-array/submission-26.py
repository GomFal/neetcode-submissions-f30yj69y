class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            
            # First check on which part of the array we are on 
            
            # If we are on the left of the array
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if target > nums[r] or target < nums[m]:
                    r = m-1
                else:
                    l = m+1
        return -1
                


            


        
        