class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSeq = 0
        numSet = set(nums)
        for num in nums:
            if num-1 not in numSet:
                seqLen = 0
                while num in numSet:
                    seqLen += 1
                    num += 1
                maxSeq = max(maxSeq, seqLen)
        return maxSeq
     