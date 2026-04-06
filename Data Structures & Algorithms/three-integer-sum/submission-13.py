class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            
            if nums[i] > 0:
                break

            if i > 0 and nums[i-1] == nums[i]:
                continue
            num = nums[i]
            j = i+1
            k = len(nums)-1
            while j<k:
                if num + nums[j] + nums[k] < 0:
                    j += 1

                elif num + nums[j] + nums[k] > 0:
                    k -= 1

                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j<k:
                        j += 1
                 
        return res



