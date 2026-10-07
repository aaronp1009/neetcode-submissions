class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Link the key to the node itself
        self.left, self.right = Node(0, 0), Node(0, 0)

        # Point at each other
        self.left.nxt = self.right
        self.right.prev = self.left

    # Remove specific node, update pointers to it
    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    # Add to the right, indicating most recently used
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.nxt = nxt.prev = node # The previous needs to point here, and the next needs to as well

        # Our node should point the the correct previous and next
        node.prev = prev
        node.nxt = nxt

    def get(self, key: int) -> int:
        # Check if it is in the cache
        if key in self.cache:
            self.remove(self.cache[key]) # since our cache holds the nodes, this is removing a node
            self.insert(self.cache[key]) # Insert again so that it becomes a most recently used

            # Actually return the value now
            return self.cache[key].val
        
        # It didn't exist in our cache
        return -1
        
    def put(self, key: int, value: int) -> None:
        # Put into cache, evict old

        # First check our cache
        if key in self.cache:
            # We need to remove it from cache
            self.remove(self.cache[key])

        # Now we add the new one
        self.cache[key] = Node(key, value)

        # Now insert it so it becomes most recently used
        self.insert(self.cache[key])

        # Now check capacity
        if len(self.cache) > self.cap: # We need to evict LRU
            lru = self.left.nxt # This is the one after your dummy left node

            # So remove/evict this
            self.remove(lru)

            # Now clean up our cache
            del self.cache[lru.key] # This is the key to remove from our cache
        
