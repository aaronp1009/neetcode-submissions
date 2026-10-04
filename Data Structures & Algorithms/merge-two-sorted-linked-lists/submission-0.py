# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node for simplicity
        dummy = ListNode()
        tail = dummy # Start at the dummy for now

        while list1 and list2:
            if list1.val < list2.val:
                # Choose this for our output
                tail.next = list1
                list1 = list1.next # Increment the list1 pointer
            else: # The other case, list2 is equal or less
                tail.next = list2
                list2 = list2.next
            # Increment our tail
            tail = tail.next
        
        # Get the remaining of one is larger than the other
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        # Since dummy is our first node, return dummy.next
        return dummy.next