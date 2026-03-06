class MyHashSet:

    def __init__(self):
        self.input = []

    def add(self, key: int) -> None:
        if key not in self.input:
            self.input.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.input:
            self.input.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.input
    
if __name__=="__main__":
    obj = MyHashSet()
    # obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    obj.remove(2)
    param_3 = obj.contains(1)
    print(param_3)