# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def zigzagdfs(node, direction, depth):
            if not node:
                return 
            
            self.longest = max(self.longest, depth)
            if direction == "left":
                zigzagdfs(node.left, "right", depth + 1)
                zigzagdfs(node.left, "left", 0)
            else:
                zigzagdfs(node.right, "left", depth + 1)
                zigzagdfs(node.right, "right", 0)
        
        zigzagdfs(root, "left", 0)
        zigzagdfs(root, "right", 0)

        return self.longest



