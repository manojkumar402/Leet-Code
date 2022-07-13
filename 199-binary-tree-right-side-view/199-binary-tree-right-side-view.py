# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root == None:
            return ans
        def rightV(root, level):
            if root == None:
                return
            if level == len(ans):
                ans.append(root.val)
            rightV(root.right, level+1)
            rightV(root.left, level+1)
        rightV(root, 0)
        return ans
        