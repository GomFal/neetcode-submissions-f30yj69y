class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        
        need = len(set(t))
        have = 0
        min_len = float("infinity")
        tCount = {}
        window = {}
        res = [-1,-1]
        for i in range(len(t)):
            tCount[t[i]] = tCount.get(t[i],0) + 1
        
        l,r = 0,0
        while r < len(s):
            window[s[r]] = window.get(s[r],0) + 1
            if s[r] in tCount and window[s[r]] == tCount[s[r]]:
                have += 1

            while need == have:
                if (r-l+1 < min_len):
                    res = [l,r]
                min_len = min(min_len, r-l+1)
                print("res: ", res, "string: ", s[l:r])
                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] + 1 == tCount[s[l]]:
                    have -= 1
                l += 1

            r += 1

        l,r = res

        return s[l:r+1]