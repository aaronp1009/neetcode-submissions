# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Use a dummy node for edge cases, this will be before head and is used to keep track of the node before left
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head # cur is going to be where our left ends up

        # Find the left
        for i in range(left-1):
            leftPrev = cur # Store the previous
            cur = cur.next # Increment current

        # leftPrev is now the node BEFORE the left, cur is the node to start reversal from
        # set prev to none, keeps track of previous node for reversal
        prev = None
        for i in range(right-left+1):
            tmp = cur.next # Store the next, we are going to break the link
            cur.next = prev # The current's node next should point to the previous (reversal)
            prev = cur # Update previous to current now for next iteration
            cur = tmp # Use our temp to move to the next node
        
        # cur will now be the node after the right, prev will be the one before right

        # leftPrev.next is left, leftPrev.next.next is whatever the left node is pointing to. Set this to the node after right (cur)
        leftPrev.next.next = cur

        # Now set the leftPrev's next to be the right node, which prev is holding a pointer to
        leftPrev.next = prev

        # Now we can return the dummy.next since that is our head

        return dummy.next