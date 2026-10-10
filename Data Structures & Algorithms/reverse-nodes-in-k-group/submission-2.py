# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # We want a dummy node
        dummy = ListNode(0, head)
        groupPrev = dummy # start at dummy

        while True:
            kth = self.getKth(groupPrev, k) # Start at node before real group
            if not kth:
                break # this is our exit condition
            
            # Store the next node of the next group
            groupNext = kth.next

            # Reverse current group
            prev, curr = kth.next, groupPrev.next # Starting node after "dummy" for understanding
            while curr != groupNext: # Go until the next group
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp # Simple reversal

            # Update the pointers, use dummy as example
            tmp = groupPrev.next # This is the node after dummy
            groupPrev.next = kth # This is the last node of this group
            groupPrev = tmp # This node that was after the dummy, is not the last node for the prev group
        
        # dummy.next is set up to point to the reversed groups
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next # Keep iterating to find the kth node
            k -= 1 # Reduce k to end loop

        # Current node is the kth node
        return curr
