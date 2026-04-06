class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            num = nums[i]
            if i > 0 and num == nums[i-1]:
                continue
            if num > 0:
                break
            l, r = i+1, len(nums)-1
            while l < r:
                if num + nums[l] + nums[r] > 0:
                    r -= 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1

                elif num + nums[l] + nums[r] < 0:
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                else:
                    print(i, l, r)
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r-=1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
        
        return res

