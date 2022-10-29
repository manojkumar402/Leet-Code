# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.solve(root)
        return self.res
    
    def solve(self, root):
        if root == None:
            return [-1,-1]
        
        left = self.solve(root.left)
        right = self.solve(root.right)
        
        if left[0] != -1:
            self.res = max(self.res, abs(root.val - left[0]))
        if left[1] != -1:
            self.res = max(self.res, abs(root.val - left[1]))
        if right[0] != -1:
            self.res = max(self.res, abs(root.val - right[0]))
        if right[1] != -1:
            self.res = max(self.res, abs(root.val - right[1]))

        # [-1,-1] , [-1,-1] val = 4
        
        ans = [-1,-1]
        if left[0] == -1 and right[0] == -1:
            ans[0] = root.val
            ans[1] = root.val
        elif left[0] != -1 and right[0] != -1:
            ans[0] = min(left[0], right[0], root.val)
            ans[1] = max(left[1], right[1], root.val)
        elif left[0] == -1:
            ans[0] = min(right[0], root.val)
            ans[1] = max(right[1], root.val)
        else:
            ans[0] = min(left[0], root.val)
            ans[1] = max(left[1], root.val)
        return ans
    