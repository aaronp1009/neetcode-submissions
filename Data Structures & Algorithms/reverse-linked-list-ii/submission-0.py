# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Use a dummy node for convenience, we need to find our leftPrev and our left
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head # We will track the node right before left for pointer updates later

        for i in range(left - 1): # 1-indexed so we need to subtract 1
            # Traverse
            leftPrev = cur
            cur = cur.next
        
        # Now our cur contains the left pointer, and leftPrev stores the node before, reverse up to the right
        prev = None
        for i in range(right-left+1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp # keep moving forward
        
        # Update our pointers, cur is pointing to the node after the right, leftPrev still points to one before left
        leftPrev.next.next = cur # point the left.next to the cur
        # Now leftPrev is still pointing to the left, but it should point to the right node, which is in prev
        leftPrev.next = prev

        # Now return dummy.next since that is the head
        return dummy.next

        

