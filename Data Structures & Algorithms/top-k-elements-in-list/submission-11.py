class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_nums = {}
        res = []
        for num in nums:
            freq_nums[num] = freq_nums.get(num, 0) + 1
        bucket = [[] for i in range(len(nums)+1)]
        
        for num, freq in freq_nums.items():
            bucket[freq].append(num)
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res


        
        
