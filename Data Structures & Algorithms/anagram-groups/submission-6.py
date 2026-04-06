class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_anagrams = defaultdict(list)
        # Hash of (tuple):[list] 
        for string in strs:
            key = [0]*26
            for c in string:
                key[ord(c) - ord('a')] += 1
            grp_anagrams[tuple(key)].append(string)
        return list(grp_anagrams.values())