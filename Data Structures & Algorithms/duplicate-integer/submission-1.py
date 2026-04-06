class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_nums = []
        for x in nums:
            if x in seen_nums:
                return True
            seen_nums.append(x)
        return False