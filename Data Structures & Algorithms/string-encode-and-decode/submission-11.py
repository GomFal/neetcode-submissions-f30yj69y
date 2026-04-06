class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string))+"#"+string
        return res

    def decode(self, s: str) -> List[str]:
        l=r=0
        res = []
        string_len = 0
        while r < len(s):
            while not s[r] == "#":
                r += 1
            string_len = int(s[l:r])
            l = r + 1
            r = l + string_len
            res.append(s[l:r])
            l = r
        return res
