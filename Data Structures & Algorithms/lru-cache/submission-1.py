class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache  = {} # Store the key mapped to node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.nxt, self.right.prev = self.right, self.left # Point to each other initially

    # Remove this node, nothing should point to it
    def remove(self, node):
        # get prev and after
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    # Insert to the right, it is a most recently used
    def insert(self, node):
        # We are inserting on the right
        prev, nxt = self.right.prev, self.right
        prev.nxt = nxt.prev = node

        # Now make this node point properly
        node.prev, node.nxt = prev, nxt


    def get(self, key: int) -> int:
        if key in self.cache: # Remove and add it so it will be on the right
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            # Now return the actual value
            return self.cache[key].val
        
        # Otherwise we didn't find it
        return -1

    def put(self, key: int, value: int) -> None:
        # If key in cache, we need to update it
        if key in self.cache:
            self.remove(self.cache[key]) # Remove it first
        
        # Add the new node for this key
        self.cache[key] = Node(key, value)

        # insert this, this will put it on the right
        self.insert(self.cache[key])

        # Check capacity
        if len(self.cache) > self.cap:
            # Evict the LRU, which is the left side
            lru = self.left.nxt
            # Just call our remove function
            self.remove(lru)

            # Clean our cache as well
            del self.cache[lru.key]
        
