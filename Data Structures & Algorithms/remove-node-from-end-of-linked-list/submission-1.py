# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create the gap between left and right, easiest is to use a dummy node
        dummy = ListNode(0, head) # It is before the head
        left = dummy
        # Right should be head + n, so iterate for it
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1 # Decrement 1 each time
        
        # Now that the gap is the same, go until right reaches the end
        while right:
            left = left.next
            right = right.next
        
        # The pointers are where they are, left is pointing to the left of the deleted node, set it to after
        left.next = left.next.next
        # Technically, we would want to make sure the deleted node isn't pointing to anything, but it's okay
        # since we return dummy.next

        # Return dummy.next, not head since a list can contain one element while n is also 1, edge case
        return dummy.next