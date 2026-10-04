# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node for edge cases
        dummy = ListNode()
        # How we keep track of the output list nodes, start at the dummy node
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val: # Take this for our output from list1
                tail.next = list1
                # Increment list1 pointer
                list1 = list1.next
            else: # The case where list2.val is <= list1.val
                tail.next = list2
                # Increment the list2 pointer
                list2 = list2.next
            
            # Tail is incremented since we are picking a node from either list1 or list2
            tail = tail.next
        
        # Handle the remaining elements, only one of these will run at a time, take all remaining elements
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        # Since the dummy node is the 0 node, we return dummy.next
        return dummy.next
