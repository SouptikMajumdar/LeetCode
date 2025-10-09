class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        l = 0
        lastZero = -1
        for r in range(len(nums)):
            if nums[r] == 0:
                if lastZero!=-1:
                    l=lastZero+1
                lastZero=r
            res = max(res, r-l)
        return res