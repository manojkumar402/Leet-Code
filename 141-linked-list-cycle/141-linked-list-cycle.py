# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rab = head
        tor = head
        while rab and tor and rab.next and rab.next.next:
            rab = rab.next.next.next
            tor = tor.next
            if rab == tor:
                return True
        return False
        
        