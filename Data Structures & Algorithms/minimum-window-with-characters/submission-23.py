class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        if s == "" or t == "":
            return ""
        
          
        s_set = set(t)
        need = len(s_set)
        have = 0
        
        s_freq = {}
        t_freq = {}

        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1 
        
        res = [-1, -1]
        min_len = float("infinity")
        l = 0
        for r in range(len(s)):
            s_freq[s[r]] = s_freq.get(s[r], 0) + 1

            if s[r] in t and s_freq[s[r]] == t_freq[s[r]]:
                have += 1
            
            while need == have:
                if (r-l+1) < min_len:
                    res = [l, r]
                    min_len = r-l+1
                
                s_freq[s[l]] -= 1
                
                if s[l] in t and s_freq[s[l]]+1 == t_freq[s[l]]:
                    have -= 1
                
                l += 1

        l, r = res
        return s[l:r+1] if min_len != float("infinity") else ""










            











