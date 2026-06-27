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
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].value
        return -1

    def find_keys_with_similar_values(self, data) -> list:
        max_keys = list()

        max_value = max(data.values())

        for key,value in data.items():
            if value == max_value:
                max_keys.append[key]

        return max_keys

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.frequency += 1
        else:
            self.frequency[key] = 1
        self.hashmap[key] = Node(key, value)
        self.insert(self.hashmap[key])
        if len(self.hashmap) > self.capacity:
            #check for the minimum frequency and if there's any node of same minimum frequency, if there's remove the lru
            keys = self.find_keys_with_similar_values(self.frequency)
            if len(keys) == 1:
                self.remove(self.hashmap[keys[0]])
                del self.hashmap[keys[0]]
                del self.frequency[keys[0]]
            else:
                lru = self.left.next
                while lru.key not in keys:
                    lru = lru.next
                self.remove(lru)
                del self.hashmap[lru.key]
                del self.frequency[lru.key]




if __name__=="__main__":
    obj = LFUCache(2)

    obj.put(1,1)#return null
    obj.put(2,2)#return null

    obj.get(1)#return 1

    obj.put(3,3)#return null

    obj.get(2)#return -1
    obj.get(3)#return 3

    obj.put(4,4)

    obj.get(1)#return -1
    obj.get(3)#return 3
    obj.get(4)#return 4



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)