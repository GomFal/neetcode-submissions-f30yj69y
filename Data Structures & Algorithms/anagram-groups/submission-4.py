class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        grouped = defaultdict(list)
        for string in strs:
            key = [0]*26
            for i in range(len(string)):
                key[ord(string[i])-ord('a')] += 1
            grouped[tuple(key)].append(string) 
        
        return list(grouped.values())
