class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.is_alphanum(s[l]):
                l += 1
            
            while r > l and not self.is_alphanum(s[r]):
                r -= 1
            
            if (s[r].lower() != s[l].lower()):
                return False
            l += 1
            r -= 1
        return True


    def is_alphanum(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9') or
                ord('a') <= ord(c) <= ord('z'))