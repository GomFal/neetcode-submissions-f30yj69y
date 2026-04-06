class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            s_ordered = ''.join(sorted(s))
            res[s_ordered].append(s)
        return list(res.values())