# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        d = deque()
        ans = []
        if root == None:
            return ans
        d.append(root)
        d.append(None)
        new = []
        while len(d) > 0:
            tmp = d[0]
            d.popleft()
            # print(tmp.val)
            if tmp == None:
                ans.append(new)
                new = []
                if len(d) > 0:
                    d.append(None)                    
            else:
                new.append(tmp.val)
                if tmp.left != None:
                    d.append(tmp.left)
                if tmp.right != None:
                    d.append(tmp.right)
        final = []
        for each in ans:
            final.append(max(each))
        return final
        