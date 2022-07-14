# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def rec(root, height):
            if root == None:
                return 0
            
            left = rec(root.left, height+1)
            right = rec(root.right, height+1)
            if None in [root.left, root.right]:
                return max(left, right)+1
            else:
                return min(left, right)+1
        return rec(root, 0)