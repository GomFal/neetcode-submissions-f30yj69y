class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]  # Buckets for each frequency. We add +1 because bucket[0] is frequency 0.
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for i, f in freq.items():
            bucket[f].append(i)
        

        res = []
        for i in range(len(bucket)-1, 0, -1):
            
            for c in bucket[i]:
                res.append(c)
                if len(res) == k:
                    return res
                    

        
        
