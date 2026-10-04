# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            # Store the next in a temp variable for next iteration
            nextTemp = cur.next

            # Make the next our previous, essentially reversing
            cur.next = prev

            # Update our previous to be the current node now
            prev = cur

            # We want to go to the next node, use the temp
            cur = nextTemp
        
        # head contains answer
        return prev