# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #def leafSimilar(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
    #    return (f:=lambda n:f(n.left)+f(n.right) or [n.val] if n else [])(r1)==f(r2)
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return False

        leaves1, leaves2 = [], []
        def getLeafValues(root, leaves):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)
            else:
                getLeafValues(root.left, leaves)
                getLeafValues(root.right, leaves)

            
        getLeafValues(root1, leaves1)
        getLeafValues(root2, leaves2)

        return leaves1 == leaves2

        
        