# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        path = []
        self.c = 0
        def rec(root, t, path):
            if root == None:
                return
            
            path.append(root.val)
            rec(root.left, t, path)
            rec(root.right, t, path)
            s = 0
            for i in range(len(path)-1,-1,-1):
                s = s + path[i]
                if s == t:
                    self.c +=1
            path.pop()
        rec(root, targetSum, path)
        return self.c