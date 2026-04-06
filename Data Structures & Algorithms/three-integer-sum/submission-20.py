class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        for i in range(len(nums)-1):
            l, r = i+1, len(nums)-1

            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1

                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                    
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    while nums[r+1] == nums[r] and l < r:
                        r -= 1
        return res


                


