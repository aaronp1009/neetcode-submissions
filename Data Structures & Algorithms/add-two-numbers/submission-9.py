# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        while l1 or l2 or carry:
            # If no node, treat as a 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry # Consider our carry
            carry = val // 10 # This will be the carry for future iterations
            val = val % 10 # This is the remainder after dividing by 10, will be our new node
            cur.next = ListNode(val) # Since we start at dummy, create a new node

            # Update pointers
            l1 = l1.next if l1 else None # None will be treated as 0 next iteration
            l2 = l2.next if l2 else None 
            cur = cur.next # Set to the next node, traversing

            # Carry is handled in loop condition
        
        return dummy.next # Node after our dummy is the real head