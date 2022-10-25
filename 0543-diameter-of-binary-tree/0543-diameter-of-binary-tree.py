# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        self.heightTree(root, res)
        return res[0]
        
    def heightTree(self, root, dia):
        if root == None:
            return 0
        
        lh = self.heightTree(root.left, dia)
        rh = self.heightTree(root.right, dia)
        
        dia[0] = max(dia[0], lh + rh)
        return 1 + max(lh, rh)
    
    """
    TC : O(N)
    SC : O(N)
    """
    