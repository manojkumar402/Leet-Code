# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """"""
        f = headA
        s = headB
        tmp = set()
        while f:
            tmp.add(f)
            f = f.next
        while s:
            if s in tmp:
                return s
            s = s.next
                        
        # return "No intersection"
        