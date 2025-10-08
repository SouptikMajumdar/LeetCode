class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, max_len, zeroes = 0, 0, 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes = zeroes + 1
            if zeroes > k:
                if nums[l] == 0:
                    zeroes = zeroes - 1
                l = l + 1
            max_len = max (max_len, r-l + 1)
        return max_len

