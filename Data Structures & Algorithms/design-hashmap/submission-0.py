class ListNode:
    def __init__(self, key = -1, value = -1):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.map = [ListNode(0) for i in range(1001)]
        self.size = 1001

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        cur = self.map[index]

        while cur.next:
            if cur.next.key == key:
                cur.next.value = value # Exists so update
                return
            cur = cur.next
        
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        cur = self.map[index]

        while cur.next:
            if cur.next.key == key:
                return cur.next.value # Found the key, return the value
        
            cur = cur.next
        
        return -1 # Did not find the key, return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        cur = self.map[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next # Just point to the next
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)