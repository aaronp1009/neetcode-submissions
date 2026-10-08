# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Handle edge case where lists is null or empty
        if not lists or len(lists) == 0:
            return None
        
        # Handle merging each list
        while len(lists) > 1: # We only expect 1 resulted merged list, keep doing this until then
            mergedLists = [] # To keep track of current merged lists
            for i in range(0, len(lists), 2): # Go by 2 lists at a time
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None # Need to handle odd cases for the loop near end
                mergedLists.append(self.mergeLists(l1, l2)) # pass these two lists into here to get a sorted merged one
            lists = mergedLists # Keep updating our lists, this will be used to exit loop...
        
        # We only have one list left, so return that
        return lists[0]


    # Helper to merge two lists in sorted order
    def mergeLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy # Keep track, starting at dummy

        while l1 and l2:
            if l1.val < l2.val: # l1.val is smaller
                tail.next = l1
                l1 = l1.next # increment l1 pointer
            else: # l2.val is smaller or equal
                tail.next = l2
                l2 = l2.next # increment l2 pointer
            tail = tail.next # increment the tail
        
        # Handle the remaining elements of the longer list
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next # This contains the actual head