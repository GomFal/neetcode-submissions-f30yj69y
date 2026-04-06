class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Sliding window to solve the problem
        if len(s) < len(t):
            return ""
        
        if len(s) == 0 or len(t) == 0:
            return ""
        
        freq_t = {}
        for c in t:
            freq_t[c] = freq_t.get(c, 0) + 1
        
        need = len(freq_t)
        have = 0

        # Use need and have to know when we have the characters
        l = 0
        res = [-1, -1]
        min_len = float("infinity")

        freq_window = {}

        for r in range(len(s)):
            freq_window[s[r]] = freq_window.get(s[r], 0) + 1

            if s[r] in freq_t and freq_window[s[r]] == freq_t[s[r]]:
                have += 1
            
            while need == have:
                if (r-l+1) < min_len:
                    res = [l, r]
                    min_len = r-l+1
                    print(s[l:r+1])
                freq_window[s[l]] -= 1
                
                if s[l] in freq_t and freq_window[s[l]] < freq_t[s[l]]:
                    
                    have -= 1
                    print(True, need, have)
                l += 1
        
        l, r = res
        res = s[l:r+1]
        return res if min_len != float("infinity") else ""
            





            











