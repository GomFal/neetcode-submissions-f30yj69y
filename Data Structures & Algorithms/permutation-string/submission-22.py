class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        if s1 == "" or s2 == "":
            return False
        
        s1_freq = [0]*26
        window_freq = [0]*26

        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            window_freq[ord(s2[i]) - ord('a')] += 1
        
        count = 0
        for i in range(26):
            if s1_freq[i] == window_freq[i]:
                count += 1
        
        if count == 26:
            return True

        l = 0
        for r in range(len(s1),len(s2)):
            
            index = ord(s2[r]) - ord('a')
            window_freq[index] += 1
            if window_freq[index] == s1_freq[index]:
                count += 1
            elif window_freq[index]-1 == s1_freq[index]:
                count -= 1
            

            index = ord(s2[l]) - ord('a')
            window_freq[index] -= 1
            if window_freq[index] == s1_freq[index]:
                count += 1
            elif window_freq[index]+1 == s1_freq[index]:
                count -= 1
            
            l += 1

            if count == 26:
                return True
            
            if s2[r] == "e":
                print(window_freq, s1_freq)
        
        return False
        

            
        


            
            




            

            


        

            

        