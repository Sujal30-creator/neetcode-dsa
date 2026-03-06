class MyHashMap:
    def __init__(self):
        self.input = list()

    def put(self, key: int, value: int) -> None:
        if not self.input:
            self.input.append([key,value])
        else:
            for element in self.input:
                if element[0] == key:
                    element[1] = value
                    return
            self.input.append([key, value])

    def get(self, key: int) -> int:
        for element in self.input:
            if element[0] == key:
                return element[1]
        return -1

    def remove(self, key: int) -> None:
        for element in self.input:
            if element[0] == key:
                self.input.remove(element)
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)