# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Use fast and slow pointer technique to get the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow.next now points to the start of the second half for us
        prev, second = None, slow.next

        # slow is the end of the first, let's point it to None/NULL to break our list into two parts
        slow.next = None

        # We want to reverse the second half now
        while second:
            tmp = second.next # Store since we will break the link
            second.next = prev
            prev = second
            second = tmp # Move onto the next node that we need to reverse links for
        
        # prev is now pointing at the last node since second is None/NULL
        first, second = head, prev

        # Since second is smaller, go through it
        while second:
            # store the parts we will remove links for
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1 # the second next will point to the first next
            first, second = tmp1, tmp2



