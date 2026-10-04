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
        # Make a hashmap mapping the old nodes to a deep copy
        oldToCopy = { None : None } # Handles the edge cases where a node.next or node.random is None

        # Loop first to map the old nodes to a deep copy in our hashmap
        cur = head
        while cur:
            oldToCopy[cur] = Node(cur.val) # Create a new node that is a copy and store it in the hashmap
            cur = cur.next
        
        # Second pass will add the links
        cur = head
        while cur:
            copy = oldToCopy[cur] # easier to read for following lines, get our copy
            copy.next = oldToCopy[cur.next] # Whatever this is in our hashmap, get the copy for it
            copy.random = oldToCopy[cur.random] # Same as above
            cur = cur.next
        
        # Now return the head of the copy, again our hashmap gets that for us in O(1) time
        return oldToCopy[head]