class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indices = {}
        for i, n in enumerate(nums):
            objective = target - n 
            if objective in nums_indices:
                return [nums_indices[objective], i]
            else:
                nums_indices[n] = i
        
