class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        freq_t = {}

        for c in t:
            freq_t[c] = freq_t.get(c, 0) + 1

        window_freq = {}
        need = len(freq_t)
        have = 0

        min_len = float("infinity")
        res = [-1,-1]

        l = 0
        for r in range(len(s)):
            char = s[r]
            window_freq[char] = window_freq.get(char, 0) + 1 
            if char in freq_t and window_freq[char] == freq_t[char]:
                have += 1
            
            while need == have:
                if (r-l+1) < min_len:
                    res = [l,r]
                    min_len = r-l+1

                char = s[l]
                window_freq[char] -= 1
                if char in freq_t and window_freq[char] < freq_t[char]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if min_len != float("infinity") else ""
            











