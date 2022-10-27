# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.solve(root)
        return self.count
    
    def solve(self, root):
        if root == None:
            return 0
        
        self.count += 1
        
        self.solve(root.left)
        self.solve(root.right)
        