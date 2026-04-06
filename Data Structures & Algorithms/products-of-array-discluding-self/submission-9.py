class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_res = [1]*len(nums)

        left_int = 1
        for i in range(len(nums)):
            array_res[i] = left_int
            left_int *= nums[i]
        
        right_int = 1
        for i in range(len(nums)-1, -1, -1):
            array_res[i] *= right_int
            right_int *= nums[i]  

        return array_res
        

        