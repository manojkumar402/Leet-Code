# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        a =  self.fast(root)
        return a[0]
    def fast(self, root: Optional[TreeNode]):
        if root == None:
            p = [True,0]
            return p
        left = self.fast(root.left)
        right = self.fast(root.right)
        
        leftAns = left[0]
        rightAns = right[0]
        diff = False
        if abs(left[1] - right[1]) <= 1:
            diff = True
        ans = [0,0]
        if leftAns and rightAns and diff:
            ans[0] = True
        else:
            ans[0] = False
        ans[1] = max(left[1], right[1]) + 1
        
        return ans
        