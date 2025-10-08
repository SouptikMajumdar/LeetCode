class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = k
        window_s = sum(nums[:k])
        max_s = window_s
        while i < len(nums):
            window_s +=  nums[i] - nums[i-k]
            if window_s > max_s:
                max_s = window_s
            i += 1
        return max_s / k
