class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        objective = 0
        for i in range(len(nums)):
            objective = target - nums[i]
            if objective in seen:
                return [seen[objective], i]
            else:
                seen[nums[i]] = i
        
        return False