class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary with pair key:values of value:index
        seen = {}
        for i, n in enumerate(nums):
            objective = target - n
            if objective in seen:
                return [seen[objective], i]
            seen[n] = i
        
        
