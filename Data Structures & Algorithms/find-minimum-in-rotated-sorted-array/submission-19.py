class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        min_num = nums[l]
        while l <= r:

            m = (l+r)//2
            min_num = min(min_num, nums[m])

            if nums[l] <= nums[r]:
                min_num = min(min_num, nums[l])
                break

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return min_num




            



        
