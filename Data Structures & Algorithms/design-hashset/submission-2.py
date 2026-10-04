class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10001)]
        self.size = 10001

    def add(self, key: int) -> None:
        index = key % self.size
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                return # Key already exists
            cur = cur.next

        # We reached empty node
        cur.next = ListNode(key)        

    def remove(self, key: int) -> None:
        index = key % self.size
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next # Handles in between
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        index = key % self.size
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)