class Node:
    def __init__(self, key, value) -> None:
        self.key, self.value = key, value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = dict()
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    #remove a node from the list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    #insert a node at the end of the list
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        self.hashmap[key] = Node(key,value)
        self.insert(self.hashmap[key])
        if len(self.hashmap) > self.capacity:
            # remove from the list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.hashmap[lru.key]

if __name__=="__main__":
    # 1. Initialize Cache with capacity 2
    print("Initializing LRUCache with capacity 2...")
    obj = LRUCache(2) 

    # 2. Put (1, 1) -> Cache: {1=1}
    print("Put (1, 1)")
    obj.put(1, 1)

    # 3. Put (2, 2) -> Cache: {1=1, 2=2}
    print("Put (2, 2)")
    obj.put(2, 2)

    # 4. Get 1 -> Returns 1. Cache: {2=2, 1=1} (1 is now MRU)
    print(f"Get 1: {obj.get(1)}") 

    # 5. Put (3, 3) -> Capacity full! Evicts LRU (2). Cache: {1=1, 3=3}
    print("Put (3, 3) -> This should evict key 2")
    obj.put(3, 3)

    # 6. Get 2 -> Returns -1 (because 2 was evicted)
    print(f"Get 2: {obj.get(2)}") 

    # 7. Put (4, 4) -> Capacity full! Evicts LRU (1). Cache: {3=3, 4=4}
    print("Put (4, 4) -> This should evict key 1")
    obj.put(4, 4)

    # 8. Get 1 -> Returns -1 (because 1 was evicted)
    print(f"Get 1: {obj.get(1)}") 

    # 9. Get 3 -> Returns 3. Cache: {4=4, 3=3}
    print(f"Get 3: {obj.get(3)}")

    # 10. Get 4 -> Returns 4.
    print(f"Get 4: {obj.get(4)}")



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)