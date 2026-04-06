class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use hash map which it's key is the freq of each letter in the alphabet (26 english letters)
        anagrams_grouped = defaultdict(list)

        for string in strs:
            freq = [0]*26
            for c in string:
                freq[ord(c) - ord('a')] += 1
            
            anagrams_grouped[tuple(freq)].append(string)
        
        return list(anagrams_grouped.values())
            