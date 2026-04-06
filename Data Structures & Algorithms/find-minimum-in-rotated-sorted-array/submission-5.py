class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[l]
        while l <= r:
            m = (l+r)//2
            print(m)
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                r = m - 1
            elif nums[l] <= nums[m]:
                # We can check to the right, because there will be smaller numbers
                res = min(res, nums[l])
                l = m + 1
            else:
                res = min(res, nums[m])
                r = m - 1
        return res
