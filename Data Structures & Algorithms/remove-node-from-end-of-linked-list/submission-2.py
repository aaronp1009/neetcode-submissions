# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use the gap technique with a left and right pointer, left is left of the node to delete
        dummy = ListNode(0, head)
        left = dummy # Start before head
        right = head

        # Need to iterate to do head + n
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # Now go to the end of the list, left will be one before node to delete
        while right:
            left = left.next
            right = right.next
        
        # Now, let's do things the right way, make sure left.next.next is stored in tmp, then point left.next to null
        left.next = left.next.next

        # Return dummy.next since this handles edge cases
        return dummy.next