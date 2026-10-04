# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Get the size
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        
        i = 0
        prev, cur = None, head
        removeIndex = count-n
        if removeIndex == 0:
            return head.next

        while i < (count-n):
            prev = cur
            cur = cur.next
            i += 1
        
        # Previous points to the node before, current is the node to remove, make prev.next point to cur.next
        # cur point to nothing
        prev.next = cur.next if cur else None
        cur = None
        
        return head