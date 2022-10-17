# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root.left, root.right)
    
    def solve(self, left, right):
        if left == None and right == None:
            return True
        if left and right and left.val != right.val:
            return False
        l, r = None, None
        if left and right:
            l = self.solve(left.right, right.left)
            r = self.solve(left.left, right.right)

        return l and r