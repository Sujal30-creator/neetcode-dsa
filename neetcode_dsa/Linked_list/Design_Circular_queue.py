class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None

class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.arr = list()
        
    def enQueue(self, value: int) -> bool:
        if len(self.arr) <= self.capacity:
            if len(self.arr) == 0:
                start = Node(value)
                end = start
            else:
                end.next = Node(value)
                end.next.prev = end
                end = end.next

            self.arr.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        pass

    def Front(self) -> int:
        pass

    def Rear(self) -> int:
        pass

    def isEmpty(self) -> bool:
        pass

    def isFull(self) -> bool:
        pass


if __name__=="__main__":
    #Initializing the queue with size 3
    obj = MyCircularQueue(3)

    #Inserting elements
    print(obj.enQueue(1))
    print(obj.enQueue(2))
    # obj.enQueue(3)
    # obj.enQueue(4)

    #Finding the rear element
    # obj.Rear()

    #Finding the queue is full?
    # obj.isFull()
