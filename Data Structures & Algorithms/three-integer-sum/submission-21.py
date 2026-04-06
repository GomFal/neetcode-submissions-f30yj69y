class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        for i in range(len(nums)):
            num = nums[i]
            
            if num > 0:
                break
            
            if i > 0 and nums[i-1] == num:
                continue
            
            l, r = i+1, len(nums)-1

            
            while l < r:
                print(num, nums[l], nums[r], num+nums[l]+nums[r])
                if (num + nums[l] + nums[r]) > 0:
                    r -= 1
                elif (num + nums[l] + nums[r]) < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
            
        return res



                


