class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l, r = 0, 0
        window_set = set()
        while r < len(s):
            while s[r] in window_set:
                window_set.remove(s[l])
                l += 1
            window_set.add(s[r])
            max_len = max(r-l+1, max_len)
            r += 1
        return max_len

        