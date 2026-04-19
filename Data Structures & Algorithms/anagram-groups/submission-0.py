class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = dict()
        for s in strs:
            sort_s = "".join(sorted(s))
            if sort_s in hmap:
                hmap[sort_s].append(s)
            else:
                hmap[sort_s] = [s]
        return list(hmap.values())