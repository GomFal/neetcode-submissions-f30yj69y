class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL=0
        window = set()
        l,r = 0,0
        
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            maxL = max(r-l+1,maxL)
        return maxL
            
