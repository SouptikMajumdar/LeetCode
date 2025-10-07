class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a, b = float(inf), float(inf)
        i = 0
        while i < len(nums):
            if nums[i] <= a:
                a = nums[i]
            elif nums[i] <= b:
                b = nums[i]
            else:
                return True
            i = i + 1
        return False
            
