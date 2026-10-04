class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.map = [ListNode(0, 0) for i in range(1009)]
        self.size = 1009

    def getCur(self, key: int) -> int:
        index = key % self.size
        return self.map[index]

    def put(self, key: int, value: int) -> None:
        cur = self.getCur(key)

        while cur.next:
            if cur.next.key == key:
                # We found pre-existing
                cur.next.value = value
                return
            cur = cur.next
        
        # We need to make a new one
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.getCur(key)

        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1 # Did not find

    def remove(self, key: int) -> None:
        cur = self.getCur(key)

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next # handles middle nodes
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)