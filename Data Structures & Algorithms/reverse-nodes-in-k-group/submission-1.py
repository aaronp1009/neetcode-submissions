# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # We want a dummy node for edge cases
        dummy = ListNode(0, head) # This is right before head
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k) # Pass in groupPrev because this is the node before next group
            # This could be null, if so, end the while loop
            if not kth:
                break
            
            # Now this is when kth is not null, it's an actual node
            groupNext = kth.next # The next node after kth is the first for the next group
            
            # do a reversal for current group, we point to kth.next because it's not guaranteed that will be reversed
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext: # Stop when reaching the next group
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp # Use the stored variable

            # pointer updates, use dummy node as example to understand
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        # Return head
        return dummy.next
    

    def getKth(self, curr, k):
        # Keep going until k is 0 or curr exists
        while curr and k > 0:
            curr = curr.next
            k -= 1 # Reduce k for loop to end
        
        # return that kth node
        return curr
