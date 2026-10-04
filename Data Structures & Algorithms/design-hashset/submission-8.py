class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for i in range(10000)]
        self.size = 10000

    def getCurrent(self, key: int) -> int:
        index = key % self.size
        return self.set[index]

    def add(self, key: int) -> None:
        cur = self.getCurrent(key)

        while cur.next:
            if cur.next.key == key:
                return # Key already exists, no need create
            cur = cur.next

        cur.next = ListNode(key)
        
    # (Node 0)
    # Dummy (ListNode(0)) -> Actual Node (ListNode(key)) -> None
    def remove(self, key: int) -> None:
        cur = self.getCurrent(key)

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next # handles the nodes in between
                return # Key already exists, no need create
            cur = cur.next
        

    def contains(self, key: int) -> bool:
        cur = self.getCurrent(key)

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