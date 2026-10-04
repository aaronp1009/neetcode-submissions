"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a hashmap that contains the mapping between the real to copy
        oldToCopy = { None : None } # Handles edge case where a next or random is None

        # Loop first time
        cur = head
        while cur:
            oldToCopy[cur] = Node(cur.val) # Create a new deep copy and store it in Hashmap, mapping real to copy
            cur = cur.next # To get to the end
        
        # Second pass to create the links now that all nodes exist in our hashmap
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            # Go through linked list
            cur = cur.next
        
        # Return the head, which again we can use our mapping to get the copy's head
        return oldToCopy[head]