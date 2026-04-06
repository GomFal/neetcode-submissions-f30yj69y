class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        window_freq = {}
        max_freq = 0
        max_len = 0
        for r in range(len(s)):
            window_freq[s[r]] = window_freq.get(s[r], 0) + 1
            max_freq = max(max_freq, window_freq[s[r]])
            while ((r-l+1) - max_freq > k):
                window_freq[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len
            
            


            



        
        
        


