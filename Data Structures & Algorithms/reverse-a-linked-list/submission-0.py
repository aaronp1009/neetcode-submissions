# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # [1 -> 2 -> 3 -> 4]

        prev = None
        cur = head

        # Start from the head
        while cur:
            # Save the next node since we're going to remove the link
            nextTemp = cur.next

            # Now we can point our cur.next to the previous, reversing the link
            cur.next = prev

            # Our next previous becomes our current
            prev = cur

            # Our current is updated to the next node in the list which we lost the link for
            cur = nextTemp
            
        # Our previous holds the answer
        return prev

        