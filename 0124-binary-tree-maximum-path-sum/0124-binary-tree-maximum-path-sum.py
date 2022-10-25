# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [float('-inf')]
        self.solve(root, ans)
        return ans[0]
    
    def solve(self, root, ans):
        if root == None:
            return 0
        
        left = max(0, self.solve(root.left, ans))
        right = max(0, self.solve(root.right, ans))
        ans[0] = max(ans[0], left+right+root.val)
        return root.val + max(left, right)
        