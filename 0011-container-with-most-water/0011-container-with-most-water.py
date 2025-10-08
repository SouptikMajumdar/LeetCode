class Solution:
    def maxArea(self, height: List[int]) -> int:
        c_i_left = 0; h_left = height[0]
        c_i_right = len(height) - 1; h_right = height[-1]
        x = c_i_right - c_i_left
        max_area = (c_i_right-c_i_left) * min(h_left, h_right)
        i = 0
        j = len(height) - 1
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j-i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area
        
            