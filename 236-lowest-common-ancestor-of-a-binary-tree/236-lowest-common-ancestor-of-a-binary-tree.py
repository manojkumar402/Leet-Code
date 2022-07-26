# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # find the path first
        a = []
        b = []
        self.path(root, p, a)
        self.path(root, q, b)
        # print(a, b)
        # 2 pointer approach
        i = 0
        j = 0
        while i < len(a) and j < len(b) and a[i] == b[j]:
            i+=1
            j+=1
        return a[i-1]
    def path(self, root, k, ans):
        if root == None:
            return False
        ans.append(root)
        if root.val == k.val:
            return True

        if self.path(root.left, k, ans) or self.path(root.right, k, ans):
            return True
        ans.pop()
        return False

        