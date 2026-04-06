class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = 0

        s1_freq = [0]*26
        window_freq = [0]*26

        for r in range(len(s1)):
            s1_freq[ord(s1[r])-ord('a')] += 1
            window_freq[ord(s2[r])-ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_freq[i] == window_freq[i]:
                matches += 1
        
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            char = ord(s2[l])-ord('a')
            window_freq[char] -= 1
            if window_freq[char] + 1 == s1_freq[char]:
                matches -= 1
            elif window_freq[char] == s1_freq[char]:
                matches += 1
            
            l += 1
            
            char = ord(s2[r])-ord('a')
            window_freq[char] += 1
            if window_freq[char] - 1 == s1_freq[char]:
                matches -= 1
            elif window_freq[char] == s1_freq[char]:
                matches += 1
            
        return matches == 26
        
            

            


        

            

        