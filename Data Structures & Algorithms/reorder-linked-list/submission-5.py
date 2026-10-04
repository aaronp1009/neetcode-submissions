# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Fast and slow pointer method to get the middle
        slow, fast = head, head.next # head.next for second so slow will end up right before the second half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Slow points to the end of first half, let's first store it's next as the start of the second half, then break
        # the link
        second = slow.next
        slow.next = None

        # Now let's reverse the second half links
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # Now the prev points to the end of the second half, and the links are reversed, so now do the actual reorder
        # Since the second half is always the same or less than first and we broke the first link, we can just iterate
        # through that
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
