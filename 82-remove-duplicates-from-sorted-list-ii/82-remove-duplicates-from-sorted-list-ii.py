# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:    
        node=ListNode(0)
        node.next=head
        prev=node
        while head and head.next:
            if head.val==head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head=head.next
                prev.next=head
            else:
                prev=prev.next
                head=head.next
        return node.next
            
        