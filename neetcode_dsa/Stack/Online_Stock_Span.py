class StockSpanner:

    def __init__(self):
        self.stack = list()

    def next(self, price: int) -> int:
        counter = 1
        if not self.stack:
            self.stack.append([price, counter])
        else:
            while self.stack and price>=self.stack[-1][0]:
                stackPrice, stackCounter = self.stack.pop()
                counter += stackCounter
                
            self.stack.append([price, counter])
        return counter




if __name__=="__main__":
    obj = StockSpanner()

    print(obj.next(100))
    print(obj.next(80))
    print(obj.next(60))
    print(obj.next(70))
    print(obj.next(60))
    print(obj.next(75))
    print(obj.next(85))

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)