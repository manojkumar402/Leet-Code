# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # we can scam by taking rev of arr
        ans = []
        if root == None:
            return ans
        q = deque()
        q.append(root)
        q.append(None)
        new = []
        while len(q) > 0:
            tmp = q[0]
            q.popleft()
            if tmp == None:
                ans.append(new)
                new = []
                # prev lvl is completely traversed
                if len(q) > 0:
                    q.append(None)
            else:
                new.append(tmp.val)
                # print(tmp.val)
                if tmp.left != None:
                    q.append(tmp.left)
                if tmp.right != None:
                    q.append(tmp.right)
        i = 1
        while i < len(ans):
            ans[i] = ans[i][::-1]
            i = i+2
        return ans