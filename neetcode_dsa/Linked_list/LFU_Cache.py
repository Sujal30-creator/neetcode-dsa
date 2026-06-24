class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = None
        self.next = None

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = dict()
        self.frequency = dict()
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    #removing the node from the list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    #inserting the node in the list
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev = prev
        node.next = next

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key]) 
        else:
            self.hashmap[key] = Node(key,value)
        self.insert(self.hashmap[key])
        #if len(self.hashmap) > self.capacity:

        

if __name__=="__main__":
    pass

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)