class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}
        bucket = [[] for i in range(len(nums)+1)]
        for n in nums:
            freq[n] = freq.get(n,0) + 1
        for n, c in freq.items():
            bucket[c].append(n)
        
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
