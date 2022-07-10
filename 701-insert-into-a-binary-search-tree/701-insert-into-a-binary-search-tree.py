# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def rec(root, val):
            if root == None:
                # do something later
                node = TreeNode(val, None, None)
                return node
            # print(root.val)
            if root.val > val:
                #move left
                left = rec(root.left, val)
                if left != None:
                    root.left = left
            else:
                # move right
                right = rec(root.right, val)
                if right != None:
                    root.right = right
        if root == None:
            return TreeNode(val, None, None)
        rec(root, val)
        return root