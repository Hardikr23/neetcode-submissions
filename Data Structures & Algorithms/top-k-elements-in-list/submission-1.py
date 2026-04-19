from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        hmap = dict()
        ans = list()
        for i in nums:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i]=1
        # {1:2, 2:5, 3:2}
        set_nums = list((k,hmap[k]) for k in hmap)
        set_nums.sort(key=lambda x: x[1], reverse=True)
        for i in range(k):
            ans.append(set_nums[i][0])

        return ans
            