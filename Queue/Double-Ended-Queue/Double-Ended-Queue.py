class Deque:
    def __init__(self):
        self.capacity = 20
        self.arr = [None] * self.capacity
        self.size = 0
        self.rear = 0
        self.front = 0
    
    #implement size expansion logic later
    def pushFront(self, val):
        newFront = (self.Front + 1) % self.capacity
        self.arr[newFront] = val
        size += 1
        self.front = newFront
    
    def pushBack(self,val):
        return