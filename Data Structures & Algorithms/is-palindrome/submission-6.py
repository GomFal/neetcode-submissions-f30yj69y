class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            while not self.is_alphanumeric(s[l]) and l<r:
                l+=1
            while not self.is_alphanumeric(s[r]) and r>l:
                r-=1
            if s[l].lower() != s[r].lower():
                print(s[l],s[r])
                return False
            l+=1
            r-=1
        return True
            
    def is_alphanumeric(self, c: str) -> bool:
        return (ord('A')<=ord(c)<=ord('Z') or 
                ord('a')<=ord(c)<=ord('z') or
                ord('0')<=ord(c)<=ord('9'))

        
