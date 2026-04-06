class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_most = 1
        result = [0]*len(nums)
        for i in range(len(nums)):
            result[i] = left_most
            left_most *= nums[i]

        right_most = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right_most
            right_most *= nums[i]

        return result 