# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ptr = head
        arr = []
        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next
        s = []
        ans = []
        
        for i in range(len(arr)-1, -1,-1):
            if len(s) == 0:
                ans.append(0)
            elif len(s) > 0 and s[-1] > arr[i]:
                ans.append(s[-1])
            elif len(s) > 0 and s[-1] <= arr[i]:
                while len(s) > 0 and s[-1] <= arr[i]:
                    s.pop()
                if len(s) == 0:
                    ans.append(0)
                else:
                    ans.append(s[-1])
            s.append(arr[i])
        ans = ans[::-1]
        return ans
    