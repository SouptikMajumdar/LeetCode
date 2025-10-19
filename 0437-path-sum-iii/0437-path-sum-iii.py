# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def countPathsFrom(node, current_sum):
            if not node:
                return 0
            current_sum += node.val
            count = 1 if current_sum == targetSum else 0
            count += countPathsFrom(node.left, current_sum)
            count += countPathsFrom(node.right, current_sum)
            return count

        def traverse(node):
            if not node:
                return 0
            return (countPathsFrom(node, 0) +
                    traverse(node.left) +
                    traverse(node.right))

        return traverse(root)


#class Solution:
  #  def pathSum(self, root, targetSum):
   #     def countPathsFrom(node, current_sum):
       #     if not node:
      #          return 0
      #      current_sum += node.val
      #      count = 1 if current_sum == targetSum else 0
       #     count += countPathsFrom(node.left, current_sum)
     #       count += countPathsFrom(node.right, current_sum)
      #      return count

      #  def traverse(node):
     #       if not node:
    #            return 0
       #     return (countPathsFrom(node, 0) +
       #             traverse(node.left) +
       #             traverse(node.right))

      #  return traverse(root)

