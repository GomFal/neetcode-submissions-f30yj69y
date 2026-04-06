class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        need = len(set(t))
        have = 0

        t_freq = {}
        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1
        
        l = 0
        window_freq  = {}
        res = [-1,-1]
        min_len = float("infinity")

        for r in range(len(s)):
            window_freq[s[r]] = window_freq.get(s[r], 0) + 1
            if s[r] in t_freq and window_freq[s[r]] == t_freq[s[r]]:
                have += 1

            while need == have:
                
                if (r-l+1) < min_len:
                    min_len = r-l+1
                    res = [l, r]
                window_freq[s[l]] -= 1
                if s[l] in t_freq and window_freq[s[l]]+1 == t_freq[s[l]]:
                    have -= 1
                l += 1

        l, r = res[0], res[1]
        return s[l:r+1]







