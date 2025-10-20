# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        depthDict = {0: 0}
        rightSideList = []

        def dfs(node, depth):
            if node is None:
                return

            if depthDict.get(depth, 0) == 0:
                rightSideList.append(node.val)
                depthDict[depth] = depthDict.get(depth, 0) + 1
            
            depth = depth + 1
            dfs(node.right, depth)
            dfs(node.left, depth)
        

        dfs(root, 0)
        print(rightSideList)

        return rightSideList


        
