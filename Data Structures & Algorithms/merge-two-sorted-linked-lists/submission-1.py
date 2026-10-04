# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node
        dummy = ListNode()
        tail = dummy # Start where our tail is the dummy

        while list1 and list2:
            if list1.val < list2.val:
                # Smaller is our tail.next
                tail.next = list1
                # Increment list1
                list1 = list1.next
            else: # list2 is smaller and can work
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next