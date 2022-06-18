# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def help(root):
            if root == None:
                return
            ans.append(root.val)
            if root.left:
                help(root.left)
            if root.right:
                help(root.right)
        help(root)
        ans.sort()
        return ans[k-1]
        
        