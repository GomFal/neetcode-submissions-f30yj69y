class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        lookup = set(nums)

        for n in nums:
            if (n-1) not in lookup:
                length = 0
                while (n+length) in lookup:
                    length += 1
                longest = max(length, longest)
        return longest