class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Using a hash map:
        freq_nums = {}
        for num in nums:
            freq_nums[num] = freq_nums.get(num, 0) + 1
        
        for num, freq in freq_nums.items():
            if freq > 1:
                return num
