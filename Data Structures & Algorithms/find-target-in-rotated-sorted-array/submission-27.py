class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                # we are on the left part of the array
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                # We are on the right side of the rotated array
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1


                


            


        
        