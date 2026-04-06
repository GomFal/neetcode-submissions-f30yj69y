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

        l = 0
        res = [-1,-1]
        min_len = float("infinity")
        for r in range(len(s)):
            char = s[r]
            print(char)
            window_freq[char] = window_freq.get(char, 0) + 1
            if char in freq_t and freq_t[char] == window_freq[char]:
                have += 1
            
            while need == have:
                print(window_freq)
                if (r-l+1) < min_len:
                    res = [l, r]
                    min_len = r-l+1
                window_freq[s[l]] -= 1
                if s[l] in freq_t and  window_freq[s[l]] < freq_t[s[l]]:
                    have -= 1
                    print(need, have)
                l+=1
            
        l, r = res
        return s[l:r+1] if min_len != float("infinity") else ""











