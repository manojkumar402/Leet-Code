# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        def solve(root, low, high):
            if root == None:
                return 0
            if root.val <= high and root.val >= low:
                self.ans = self.ans + root.val
            solve(root.right, low, high)
            solve(root.left, low, high)

        solve(root,low,high)
        return (self.ans)
        
        
        