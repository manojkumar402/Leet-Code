# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        new = ListNode(0)
        s = new
        while ptr:
            if ptr.val == 0:
                ptr2 = ptr.next
                tmp = 0
                while ptr2:
                    if ptr2.val != 0:
                        tmp += ptr2.val
                        ptr2 = ptr2.next
                    else:
                        break
                # create new LL nd add
                if tmp != 0:
                    dummy = ListNode(tmp)
                    s.next = dummy
                    s = s.next
            ptr = ptr2
            
        return new.next
