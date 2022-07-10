# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def some(root):
            if root == None:
                return [0,0,0]

            left = some(root.left)
            right = some(root.right)
            count = 0
            curr = (left[0] + right[0] + root.val)
            if curr // (left[1] + right[1] + 1) == root.val:
                count = 1
                # print(root.val, left[1], right[1])
            return [curr, left[1]+right[1]+1, left[2] + right[2] + count]
        return some(root)[2]