# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def rec(root, target):
            if root == None:
                return False
            if root.left == None and root.right == None and target-root.val == 0:
                return True
            l = rec(root.left, target-root.val)
            r = rec(root.right, target-root.val)
            return l or r
        return rec(root, targetSum)