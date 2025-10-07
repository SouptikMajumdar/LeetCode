class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        pre = [1] * len(nums)
        suf = [1] * len(nums)
        i = 0
        while i+1 < len(nums):
            pre[i+1] = pre[i] * nums[i]
            i += 1
        i = len(nums) - 1
        while i > 0:
            suf[i-1] = suf[i] * nums[i]
            i -= 1
        i = 0
        while i<len(nums):
            answer[i] = pre[i] * suf[i]
            i += 1
        
        return answer           
        
