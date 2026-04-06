class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        
        freq_t, window = {}, {}

        min_len = float("infinity")
        res = [-1,-1]

        for c in t:
            freq_t[c] = freq_t.get(c,0)+1
        
        need = len(freq_t)
        have = 0

        l=0
        for r in range(len(s)):
            
            window[s[r]] = window.get(s[r],0)+1

            if s[r] in freq_t and window[s[r]] == freq_t[s[r]]:
                have += 1

            while need == have:
                if (r-l+1) < min_len:
                    min_len = r-l+1
                    res = [l,r]

                window[s[l]] -= 1 
                if s[l] in freq_t and window[s[l]] < freq_t[s[l]]:
                    have -= 1
                l+=1
        l,r = res
        return s[l:r+1]

        

        