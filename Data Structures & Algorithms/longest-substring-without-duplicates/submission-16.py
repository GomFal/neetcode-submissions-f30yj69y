class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        window_set = set()
        for r in range(len(s)):
            while s[r] in window_set:
                window_set.remove(s[l])
                l += 1
            window_set.add(s[r])
            max_len = max(r-l+1, max_len)

        return max_len 
            