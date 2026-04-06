class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        freq_t = {}
        for c in t:
            freq_t[c] = freq_t.get(c,0) + 1
        
        need = len(freq_t.keys())
        have = 0

        freq_window = {}

        res = [-1,-1]
        min_len = float("infinity")

        l = 0

        print(freq_t, need, have)

        for r in range(len(s)):
            
            freq_window[s[r]] = freq_window.get(s[r], 0) + 1
            if s[r] in freq_t and freq_window[s[r]] == freq_t[s[r]]:
                have += 1

            while need == have:
                if r-l+1 < min_len:
                    min_len = min(min_len, r-l+1)
                    res = [l, r]

                freq_window[s[l]] -= 1
                if s[l] in freq_t and freq_window[s[l]] < freq_t[s[l]]:
                    have -= 1
                l += 1
            

        l, r = res
        return s[l:r+1]








