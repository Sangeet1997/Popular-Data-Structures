class Stack:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    def push(self, val):
        if self.size == self.capacity:
            self._resize()
        self.arr[self.size] = val
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise ValueError("Stack empty.")
        temp = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        if self.size < self.capacity // 4 and self.size >= 8:
            self._resize()
        return temp

    def __len__(self):
        return self.size

    def __str__(self):
        res = "["
        for i in range(self.size):
            if i != self.size - 1:
                res = res + str(self.arr[i]) + ","
            else:
                res = res + str(self.arr[i])
        res = res + "]"
        return res

    def is_empty(self):
        if self.size:
            return False
        return True

    def peek(self):
        if self.size == 0:
            raise ValueError("Stack empty.")
        return self.arr[self.size - 1]
    
    def _resize(self):
        if self.size == self.capacity:
            self.capacity = self.capacity * 2
            new_arr = [None] * (self.capacity)
            for i, ele in enumerate(self.arr):
                new_arr[i] = ele
            self.arr = new_arr
        else:
            self.capacity = self.capacity // 2
            new_arr = [None] * (self.capacity)
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr


if __name__ == "__main__":
    # Create a new stack
    stack = Stack()
    
    # Test is_empty on new stack
    print(f"Is empty: {stack.is_empty()}")
    print(f"Length: {len(stack)}")
    print(f"Stack: {stack}")
    
    # Test push operations
    print("\n--- Testing push operations ---")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    print(f"After pushing 10, 20, 30, 40: {stack}")
    print(f"Length: {len(stack)}")
    print(f"Is empty: {stack.is_empty()}")
    
    # Test peek
    print(f"\nPeek top element: {stack.peek()}")
    print(f"Stack after peek: {stack}")
    
    # Test push to trigger resize
    print("\n--- Testing resize (push) ---")
    stack.push(50)  # This should trigger a resize
    print(f"After pushing 50: {stack}")
    print(f"Length: {len(stack)}")
    
    # Test pop operations
    print("\n--- Testing pop operations ---")
    popped = stack.pop()
    print(f"Popped: {popped}")
    print(f"Stack after pop: {stack}")
    
    popped = stack.pop()
    print(f"Popped: {popped}")
    print(f"Stack after pop: {stack}")
    
    # Test multiple pops to trigger resize down
    print("\n--- Testing resize (pop) ---")
    # Add more elements first
    for i in range(60, 90, 10):
        stack.push(i)
    print(f"After adding more elements: {stack}")
    
    # Pop elements to trigger downsize
    while len(stack) > 2:
        popped = stack.pop()
        print(f"Popped: {popped}, Stack: {stack}, Length: {len(stack)}")
    
    # Test error cases
    print("\n--- Testing error cases ---")
    # Pop remaining elements
    while not stack.is_empty():
        print(f"Popping: {stack.pop()}")
    
    print(f"Final empty stack: {stack}")
    
    try:
        stack.pop()
    except ValueError as e:
        print(f"Error when popping empty stack: {e}")
    
    try:
        stack.peek()
    except ValueError as e:
        print(f"Error when peeking empty stack: {e}")