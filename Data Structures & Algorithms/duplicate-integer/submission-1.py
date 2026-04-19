class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = dict()
        for i in nums:
            try:
                hmap[i]+=1
                return True
            except:
                hmap[i]=1
        return False