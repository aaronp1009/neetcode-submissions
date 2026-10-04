class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10000)]
        self.size = 10000

    def add(self, key: int) -> None:
        index = key % self.size # Hash to get index in set
        cur = self.set[index] # Go to the right node in the set
        
        # Travel to the end of that linked list
        while cur.next:
            # If there is already this key, it's a SET so return
            if cur.next.key == key:
                return
            cur = cur.next

        # Since this is None, set to the new node
        cur.next = ListNode(key)


    def remove(self, key: int) -> None:
        index = key % self.size # Hash to get index in set
        cur = self.set[index] # Go to the right node in the set
        
        # Travel to the second to end
        while cur.next:
            # If there is already this key, it's a SET so return
            if cur.next.key == key:
                cur.next = cur.next.next # This takes care of removing in between
                return
            cur = cur.next
        

    def contains(self, key: int) -> bool:
        index = key % self.size # Hash to get index in set
        cur = self.set[index] # Go to the right node in the set
        
        # Travel to the second to end
        while cur.next:
            # We found the key
            if cur.next.key == key:
                return True
            cur = cur.next

        # We did not find the key
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)