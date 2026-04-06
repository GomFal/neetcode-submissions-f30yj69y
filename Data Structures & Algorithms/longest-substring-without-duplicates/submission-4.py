class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL=0
        window = {}
        l,r = 0,0
        while r < len(s):
            window[s[r]] = window.get(s[r],0) + 1
            while window.get(s[r],0) > 1:
                window[s[l]] -=1
                l += 1
            maxL = max(maxL, r-l+1)
            r += 1
        return maxL
            
