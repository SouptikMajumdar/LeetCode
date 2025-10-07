class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        z_i = len(nums) - 1
        while i > 0:
            if nums[i-1] == 0 and nums[i] != 0:
                j = i-1
                while j < z_i:
                    nums[j] = nums[j+1]
                    j = j + 1
                nums[z_i] = 0
                z_i = z_i -1
            i = i - 1
            

            
              


                
        