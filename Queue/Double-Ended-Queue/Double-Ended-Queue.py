class Deque:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0
        self.rear = 0
        self.front = 0
    
    def pushFront(self, val):  # Should add to LEFT (beginning)
        if self.size == 0:
            self.arr[self.front] = val
            self.size += 1
            return
        
        # Move front leftward (decrease index)
        newFront = (self.front - 1) % self.capacity
        if newFront == self.rear and self.size > 0:
            self.resize()
            newFront = (self.front - 1) % self.capacity
        self.arr[newFront] = val
        self.size += 1
        self.front = newFront

    def pushBack(self, val):   # Should add to RIGHT (end)
        if self.size == 0: # if queue is empty
            self.arr[self.front] = val
            self.size += 1
            return
        
        # Move rear rightward (increase index)
        newRear = (self.rear + 1) % self.capacity
        if newRear == self.front and self.size > 0:
            self.resize()
            newRear = (self.rear + 1) % self.capacity
        self.arr[newRear] = val
        self.size += 1
        self.rear = newRear
        return
    
    def removeFront(self):
        if self.size == 0:
            raise ValueError("Empty dequeue.")
        
        val = self.arr[self.front]
        self.arr[self.front] = None
        self.size -= 1
        
        if self.size == 0:
            self.front = self.rear = 0
        else:
            self.front = (self.front + 1) % self.capacity  # Move front forward, not backward
        return val

    def removeRear(self):
        if self.size == 0:
            raise ValueError("Empty dequeue.")
        
        val = self.arr[self.rear]
        self.arr[self.rear] = None
        self.size -= 1
        
        if self.size == 0:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear - 1) % self.capacity  # Move rear backward, not forward
        return val
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        res = "[ "
        for i in range(self.size):
            j = (self.front + i) % self.capacity
            if i == self.size - 1:
                res = res + str(self.arr[j]) + " ]"
            else:
                res = res + str(self.arr[j]) + ", "
        return res
    
    def __getitem__(self, index):
        if index >= self.size:
            raise ValueError("Index out of bounds.")
        while index < 0:
            index = index + self.size
        index = (index + self.front) % self.capacity
        return self.arr[index]
    
    def __setitem__(self, index, val):
        if index >= self.size:
            raise ValueError("Index out of bounds.")
        while index < 0:
            index = index + self.size
        index = (index + self.front) % self.capacity
        self.arr[index] = val

    def resize(self):
        old_capacity = self.capacity
        self.capacity = self.capacity * 2
        newQueue = [None] * self.capacity

        for i in range(self.size):
            j = (self.front + i) % old_capacity
            newQueue[i] = self.arr[j]
        
        self.arr = newQueue
        self.front = 0
        self.rear = self.size - 1 if self.size > 0 else 0 
    
    def peekFront(self):
        if self.size == 0:
            raise ValueError("Empty deque")
        return self.arr[self.front]  
    
    def peekRear(self):
        if self.size == 0:
            raise ValueError("Empty deque")
        return self.arr[self.rear]   
    
    def is_empty(self):
        return self.size == 0
    
    def clear(self):
        self.arr = [None] * self.capacity
        self.front = self.rear = 0
        self.size = 0

    def __iter__(self):
        return DequeIterator(self)

class DequeIterator:
    def __init__(self, deque):
        self.deque = deque
        self.count = 0
    
    def __next__(self):
        if self.count >= self.deque.size:
            raise StopIteration
        index = (self.deque.front + self.count) % self.deque.capacity
        val = self.deque.arr[index]
        self.count += 1
        return val 
        
if __name__ == "__main__":
    print("=== Testing Deque ===")
    deque = Deque()
    
    # Test basic operations
    deque.pushBack(1)
    deque.pushBack(2)
    deque.pushFront(0)
    print(f"After pushes: {deque}")  # Should be [0, 1, 2]
    
    print(f"Front: {deque.peekFront()}")  # Should be 0
    print(f"Rear: {deque.peekRear()}")   # Should be 2
    
    print(f"Remove front: {deque.removeFront()}")  # Should be 0
    print(f"Remove rear: {deque.removeRear()}")    # Should be 2
    print(f"After removes: {deque}")  # Should be [1]
    
    # Test resize
    for i in range(10):
        deque.pushBack(i)
    print(f"After many pushes: {deque}")
    print(f"Capacity: {deque.capacity}")
    
    # Test iteration
    print("Iteration test:")
    for item in deque:
        print(item, end=" ")
    print()

