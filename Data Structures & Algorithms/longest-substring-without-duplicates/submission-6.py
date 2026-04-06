class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        window = set()
        maxLen = 0
        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            maxLen = max(maxLen, len(window))
            r += 1
        return maxLen
        