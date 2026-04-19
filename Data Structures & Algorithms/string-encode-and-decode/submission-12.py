import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        comb_str = str()
        for word in strs:
            comb_str += str(len(word)) + '#' + word
        return comb_str

    def decode(self, s: str) -> List[str]:
        all_words = list()
        i=0
        while i < len(s):
            start = i
            while s[i] != "#":
                i += 1
            length = int(s[start:i])
            i += 1 
            all_words.append(s[i:i+length])
            i += length
                
        return all_words

