class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or s == "":
            return ""
        if len(s) < len(t):
            return ""

        need = len(set(t))
        have = 0
        freq_t = {}
        freq_window = {}
        for i in range(len(t)):
            freq_t[t[i]] = freq_t.get(t[i], 0) + 1

        sol = [-1,-1]
        minLen = float("inf")

        window = {}
        l = 0
        for r in range(len(s)):
            
            freq_window[s[r]] = freq_window.get(s[r], 0) + 1
            if s[r] in freq_t and freq_window[s[r]] == freq_t[s[r]]:
                have += 1

            while need == have:
                if r-l+1 < minLen:
                    minLen = r-l+1
                    sol = [l,r+1]
                    print(minLen, sol)
                    
                freq_window[s[l]] -= 1
                if s[l] in freq_t and freq_window[s[l]] < freq_t[s[l]]:
                    have -= 1
                l += 1
        
        l,r = sol
        return s[l:r]
            


