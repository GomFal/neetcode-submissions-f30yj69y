class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        window_freq = {}
        maxf = 0
        for r in range(len(s)):
            window_freq[s[r]] = window_freq.get(s[r], 0) + 1
            maxf = max(maxf, window_freq[s[r]])

            while (r-l+1)-maxf > k:
                window_freq[s[l]] -= 1
                l += 1
            max_len = max(r-l+1, max_len)
        return max_len

            



        
        
        


