# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's tortoise and hare algorithm
        slow, fast = head, head # Start at the same spot

        # need to check fast and fast.next since fast moves by 2
        while fast and fast.next:
            slow = slow.next # Increment by 1
            fast = fast.next.next # Increment by 2

            # We found a loop
            if slow == fast:
                return True
        
        # Fast looped the entire list and never caught up to slow
        return False