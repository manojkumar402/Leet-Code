# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        left = self.sumEvenGrandparent(root.left)
        right = self.sumEvenGrandparent(root.right)
        ans = 0
        # check
        if root.val % 2 == 0:
            #check all the grand sons
            if root.right != None and root.right.right != None:
                ans += root.right.right.val
            if root.right != None and root.right.left != None:
                ans += root.right.left.val
            if root.left != None and root.left.right != None:
                ans += root.left.right.val
            if root.left != None and root.left.left != None:
                ans += root.left.left.val
            # print(ans)
        return left + right + ans