# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        depthSum = {1: 0}
        def dfs(node, depth):
            if not node:
                return
            
            depthSum[depth] = depthSum.get(depth, 0) + node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
            depth -= 1
            return
        
        dfs(root, 1)

        maxVal = max(depthSum.values())
        minDepth = min(list(filter(lambda key: depthSum[key] == maxVal, depthSum)))

        return minDepth


            


            
            
