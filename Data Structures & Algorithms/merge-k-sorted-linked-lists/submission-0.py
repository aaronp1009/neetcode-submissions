# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Handle edge cases, if lists is null or there is no list
        if not lists or len(lists) == 0:
            return None # Nothing to merge, empty list basically
        
        while len(lists) > 1: # While we have more than one list, we have to keep merging
            mergedLists = []
            for i in range(0, len(lists), 2): # Iterate through len of list in increments of 2
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None # Handles odd list lengths near end
                # call our helper
                mergedLists.append(self.mergeLists(l1, l2))
            lists = mergedLists
        
        # Now return the single list
        return lists[0]

    # Helper
    def mergeLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                # increment l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # Increment tail node
            tail = tail.next
        
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return dummy.next # Return merged list