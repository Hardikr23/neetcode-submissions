from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Option 2: custom
        if len(s) != len(t):
            return False
        s_map, t_map = dict(), dict()

        for i in range(len(s)):
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + + t_map.get(t[i], 0)
        if s_map==t_map:
            return True
        return False
        
        # Option 1: easy
        # s_map = Counter(s)
        # t_map = Counter(t)
        # if s_map == t_map:
        #     return True
        # return False
