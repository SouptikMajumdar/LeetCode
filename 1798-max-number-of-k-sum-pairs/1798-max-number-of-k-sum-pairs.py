class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0 
        num_dict = {}
        for i,n in enumerate(nums):
            rem = k - nums[i]
            if rem in num_dict:
                count += 1
                if num_dict[rem] == 1: 
                    del num_dict[rem] 
                else: 
                    num_dict[rem] -= 1
            else:
                num_dict[nums[i]] = 1 if nums[i] not in num_dict else num_dict[nums[i]] + 1
        return count

                


            
            
            
