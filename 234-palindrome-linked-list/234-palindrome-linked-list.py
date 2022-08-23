# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while(curr):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        tmp_head = head
        while(tmp_head and tmp_head!=slow and prev):
            if tmp_head.val != prev.val:
                return False
            tmp_head = tmp_head.next
            prev = prev.next
        return True
        