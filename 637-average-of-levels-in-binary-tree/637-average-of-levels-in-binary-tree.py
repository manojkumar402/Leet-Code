# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # level order traversal
        q = deque()
        q.append(root)
        q.append(None)
        ans = []
        tmp = []
        while len(q) > 0:
            node = q[0]
            q.popleft()
            if node == None:
                ans.append(tmp)
                tmp = []
                if len(q) > 0:
                    q.append(None)
            else:
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        res = []
        for each in ans:
            res.append(sum(each)/len(each))
        return res
            