# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        """
        preorder --> NLR
        inorder -->  LNR
        preorder = [3,9,20,15,7]
                   [-1, 3, 9, 20, ]
        inorder =  [9,3,15,20,7]
        3
       / \
      9   20
        
        """
        
        if not inorder or not preorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
        
        
        