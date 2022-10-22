# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        st1 = [root]
        st2 = []
        
        while len(st1) > 0:
            node = st1.pop()
            st2.append(node.val)
            if node.left:
                st1.append(node.left)
            if node.right:
                st1.append(node.right)
        return st2[::-1]
#         def postorder(root):
#             if root == None:
#                 return 
            
#             # print(root.val)
#             if root.left != None:
#                 postorder(root.left)

#             if root.right != None:
#                 postorder(root.right)
#             ans.append(root.val)
#         postorder(root)
        # return ans