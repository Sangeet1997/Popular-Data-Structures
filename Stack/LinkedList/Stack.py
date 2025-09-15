class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            raise ValueError("Stack Empty.")
        self.size -= 1
        x = self.head.val
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return x
    
    def peek(self):
        if self.size == 0:
            raise ValueError("Stack Empty.")
        return self.head.val
    
    def is_empty(self):
        return self.size == 0
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        curr = self.head
        res = ""
        while curr:
            res = res + str(curr.val) + "->"
            curr = curr.next
        return res

if __name__ == "__main__":
    print("=== Stack Implementation Testing ===\n")
    
    # Create a new stack
    stack = Stack()
    print(f"1. Created empty stack")
    print(f"   Is empty: {stack.is_empty()}")
    print(f"   Size: {len(stack)}")
    print(f"   Stack: {stack}\n")
    
    # Test push operations
    print("2. Testing push operations:")
    values = [10, 20, 30, 40, 50]
    for val in values:
        stack.push(val)
        print(f"   Pushed {val} -> Size: {len(stack)}")
    print(f"   Final stack: {stack}")
    print(f"   Is empty: {stack.is_empty()}\n")
    
    # Test peek operation
    print("3. Testing peek operation:")
    try:
        top = stack.peek()
        print(f"   Top element: {top}")
        print(f"   Stack after peek: {stack}")
        print(f"   Size unchanged: {len(stack)}\n")
    except ValueError as e:
        print(f"   Error: {e}\n")
    
    # Test pop operations
    print("4. Testing pop operations:")
    while len(stack) > 2:
        popped = stack.pop()
        print(f"   Popped: {popped} -> Size: {len(stack)}")
    print(f"   Stack after pops: {stack}\n")
    
    # Test edge cases
    print("5. Testing edge cases:")
    
    # Pop remaining elements
    while not stack.is_empty():
        popped = stack.pop()
        print(f"   Popped: {popped} -> Size: {len(stack)}")
    
    print(f"   Empty stack: {stack}")
    
    # Test operations on empty stack
    try:
        stack.peek()
    except ValueError as e:
        print(f"   Peek on empty stack: {e}")
    
    try:
        stack.pop()
    except ValueError as e:
        print(f"   Pop on empty stack: {e}")
    
    print(f"\n6. Final verification:")
    print(f"   Is empty: {stack.is_empty()}")
    print(f"   Size: {len(stack)}")
    
    print("\n=== All tests completed! ===")

