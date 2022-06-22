# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        a = self.help(root, [])
        print(a)
        if root == None:
            return []
        for i in range(1,len(a)):
            tmp = TreeNode(a[i])
            root.left = None
            root.right = None
            root.right = tmp
            root = root.right
            
        
    def help(self, ptr, new):
        if ptr == None:
            return
        new.append(ptr.val)        
        if ptr.left:
            self.help(ptr.left, new)
            
        if ptr.right:
            self.help(ptr.right, new)
            
        return new
        
    
