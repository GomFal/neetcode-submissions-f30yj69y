class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = 0
        window_mp = {}

        for r in range(len(s)):
            if s[r] in window_mp:
                l = max(window_mp[s[r]]+1, l)
            
            window_mp[s[r]] = r    
            max_len = max(r-l+1, max_len)
        return max_len

        