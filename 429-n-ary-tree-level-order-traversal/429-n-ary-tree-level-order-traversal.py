"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        q = deque()
        q.append(root)
        q.append(None)
        res = []
        new = []
       
        while len(q) > 0:
            node = q[0]

            q.popleft()
            if node == None:
                res.append(new)
                new = []
                if len(q) > 0:
                    q.append(None)
            else:
                new.append(node.val)
                for child in node.children:
                    q.append(child)
        return res
        
                