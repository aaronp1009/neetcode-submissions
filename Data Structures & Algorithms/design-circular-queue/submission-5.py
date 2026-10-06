class ListNode:
    def __init__(self, val, nxt, prev):
        # A Doubly Linked List
        self.val = val
        self.nxt = nxt
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0, None, None) # Will set later
        self.right = ListNode(0, None, self.left) # Previous is self.left
        self.left.nxt = self.right # Now that we created it, left can point to it

    def enQueue(self, value: int) -> bool:
        # Add to the right since FIFO
        # if full, no space to enqueue
        if self.isFull(): return False

        # There is space, we add to the right
        cur = ListNode(value, self.right, self.right.prev)
        self.right.prev.nxt = cur
        self.right.prev = cur
        self.space -= 1 # one less space

        return True

    def deQueue(self) -> bool:
        # Typically remove from the left, since First in First Out
        # if empty, nothing to dequeue
        if self.isEmpty(): return False

        self.left.nxt = self.left.nxt.nxt # Point two nodes after the dummy, the first one after is what we are removing
        self.left.nxt.prev = self.left # the node two after, which is now just self.left.nxt needs its previous to point to left dummy
        self.space += 1 # We created space

        return True


    def Front(self) -> int:
        # Front is the left side
        if self.isEmpty(): return -1 # Empty, nothing
        return self.left.nxt.val # left next is the front if not empty

    def Rear(self) -> int:
        # Rear is the right side
        if self.isEmpty(): return -1 # Empty, nothing
        return self.right.prev.val # The node to the left of right is the rear

    def isEmpty(self) -> bool:
        return self.left.nxt == self.right # Left dummy is pointing to right dummy, if true, empty

    def isFull(self) -> bool:
        return self.space == 0 # No more space left
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()