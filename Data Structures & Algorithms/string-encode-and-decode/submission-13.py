class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            
            j = i+1
            i = j + int(length)
            string = s[j:i]
            result.append(string)
            
            
        return result
       