class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        res = -1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            
            if nums[m] >= nums[l]: # We are on the left slice of the array
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: # Right slice of the array
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1


        
                
