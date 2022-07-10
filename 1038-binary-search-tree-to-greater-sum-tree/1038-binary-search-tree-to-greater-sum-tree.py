# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        arr = []
        d = {}
        def preorder(root, ans):
            if root == None:
                return
            ans.append(root.val)
            preorder(root.left, ans)
            preorder(root.right, ans)
        ptr = root
        preorder(ptr, arr)
        arr.sort()
        for i in range(len(arr)):
            sub = arr[i+1:]
            d[arr[i]] = sum(sub) + arr[i]
        # print(d)
        ptr2 = root
        def final(root, d):
            if root == None:
                return
            root.val = d[root.val]
            final(root.left, d)
            final(root.right, d)
        final(ptr2, d)
        return root
        
        
            

    
        