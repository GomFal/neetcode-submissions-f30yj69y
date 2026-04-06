class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        freq = [0 for i in range(26)]

        for c in s1:
            freq[ord(c) - ord('a')] += 1

        window = [0 for i in range(26)]
        
        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1
        print("window: ", window, "freq: ", freq)
        if window == freq:
            return True

        l = 0
        
        for r in range(len(s1),len(s2)):
            window[ord(s2[l]) - ord('a')] -= 1
            l += 1
            window[ord(s2[r]) - ord('a')] += 1
            if window == freq:
                return True

        return False

        