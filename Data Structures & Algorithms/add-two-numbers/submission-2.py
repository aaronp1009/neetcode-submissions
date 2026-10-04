# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ""

        cur = l1
        while cur:
            first = str(cur.val) + first
            cur = cur.next
        
        second = ""

        cur = l2
        while cur:
            second = str(cur.val) + second
            cur = cur.next
        
        new = int(first) + int(second)

        new = str(new)
        chars = list(new)

        dummy = ListNode(0)
        cur = dummy
        prev = None
        i = len(new)-1
        while cur and i >= 0:
            cur.next = ListNode(new[i])
            i -= 1
            cur = cur.next
        
        return dummy.next
