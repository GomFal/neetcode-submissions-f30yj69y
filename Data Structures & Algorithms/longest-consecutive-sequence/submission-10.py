class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set()
        max_seq = 0

        for number in nums:
            lookup.add(number)
        
        for num in nums:
            if num-1 not in lookup:
                seq = 1
                while num+seq in lookup:
                    seq += 1
                max_seq = max(seq, max_seq)
        return max_seq
                

     