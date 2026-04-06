from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        s_counter=Counter(s_list)
        t_counter=Counter(t_list)
        counter=0
        if(len(s_list) == len(t_list)):
            for char in s_counter.keys():
                if s_counter.get(char) == t_counter.get(char):
                    counter+=1
            if (len(s_counter) == counter):
                return True

        return False
        
