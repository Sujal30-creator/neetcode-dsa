class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            val_to_insert = val
        else:
            val_to_insert = min(self.min_stack[-1],val)
        self.min_stack.append(val_to_insert)

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

if __name__=='__main__':
    obj = MinStack()
    print(obj.push(-2))
    print(obj.push(0))
    print(obj.push(-3))
    print(obj.getMin())
    print(obj.pop())
    print(obj.top())
    print(obj.getMin())
        
         
        

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()