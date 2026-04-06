class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums_set = set(nums)
        maxlength = 0
        for num in nums:
            if (num-1) in nums_set:
                continue
            else:
                length = 1
                while (num+1) in nums_set:
                    length += 1
                    num += 1
                maxlength = max(maxlength, length)
        return maxlength