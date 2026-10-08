class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.nxt = None


class LinkedList:
    def __init__(self):
        # Make this doubly
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.nxt, self.right.prev = self.right, self.left
        self.size = 0

    def length(self):
        return self.size
    
    def pushRight(self, node): # Want this to push to the right, like LRU problem
        prev, nxt = self.right.prev, self.right
        prev.nxt = nxt.prev = node

        # Set the node's prev and next
        node.nxt, node.prev = nxt, prev
        
        self.size += 1

    def pop(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev
        self.size -= 1
    
    def popLeft(self):
        if self.length() == 0: # nothing to pop
            return None
        # Pop one after the dummy left node
        node = self.left.nxt # need this since we will return it
        self.pop(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCnt = 0
        self.nodeMap = {} # Map the key to the node, same as LRU problem

        # Maps frequency -> linkedlist of nodes, leftmost is LRU
        self.listMap = defaultdict(LinkedList) # Handles edge cases better

    def counter(self, node):
        # Get this node's freqency
        cnt = node.freq # We made this part of the node class

        self.listMap[cnt].pop(node) # Find the right linked list and remove it, we will add again for LRU logic

        # There was a key with this lfuCnt but now there isn't so we must increment lfuCnt
        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1
        
        node.freq += 1 # Increase our node frequency as we're going to add it
        # Add this to the correct key in our listMap, pushRight inserts to right since we want LRU on left, MRU on right
        self.listMap[node.freq].pushRight(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap: # There is no node mapped to this key
            return -1
        
        # There is a node for this key
        node = self.nodeMap[key]
        self.counter(node) # Use our counter for the LFU part
        return node.val # return the value

    def put(self, key: int, value: int) -> None:
        # Edge case, do not add if full
        if self.cap == 0:
            return

        if key in self.nodeMap: # It's already in our nodeMap, just update it
            node = self.nodeMap[key]
            node.val = value
            self.counter(node) # To comply with LFU
            return
        
        # Handle the cap
        if len(self.nodeMap) == self.cap:
            # Evict the LRU from the linkedlist mapped to the lfuCnt
            node = self.listMap[self.lfuCnt].popLeft()
            self.nodeMap.pop(node.key) # Remove this from our nodeMap as well
        
        # Add the new node into both the nodeMap and listMap
        node = ListNode(key, value)
        self.nodeMap[key] = node

        # This goes into the freq 1 bucket
        self.listMap[1].pushRight(node)
        self.lfuCnt = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)