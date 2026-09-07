class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = int(len(nums))
        if length < 1: 
            return -1
        for i in range(0,length):
            sum_left = sum(nums[:i])
            sum_right = sum(nums[i+1:])
            if sum_left == sum_right:
                return i
        return -1