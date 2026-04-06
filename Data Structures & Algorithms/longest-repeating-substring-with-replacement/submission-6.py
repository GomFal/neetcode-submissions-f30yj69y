class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        maxL = 0
        window = {}
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1
    
            while (r-l+1 - max(window.values())) > k:
                window[s[l]] -= 1
                l += 1
                
            
            
            if r-l+1 - max(window.values()) <= k:
                print("r: ", s[r])
                print("l: ", s[l])
                maxL = max(r-l+1, maxL)
                print("maxL: ", maxL)
            

        return maxL
            
