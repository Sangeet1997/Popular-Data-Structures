class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, i):
        if i >= self.size:
            raise ValueError("Index Out of bounds Error")
        
        curr = self.head
        while curr:
            if i == 0:
                return curr.val
            i -= 1
            curr = curr.next
        
        return None
    
    def insertFront(self, val):
        self.size += 1
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
            return
        
        temp = Node(val)
        temp.next = self.head
        self.head = temp
        
    def insertBack(self, val):
        self.size += 1
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
            return

        temp = Node(val)
        self.tail.next = temp
        self.tail = temp
        
    def remove(self, i):
        if i >= self.size:
            raise ValueError("Index Out of Bounds Error.")
        self.size -= 1
        j = 0
        curr = self.head
        prev = None
        while curr:
            if i == j:
                if prev == None: # first element (curr == self.head)
                    if self.head == self.tail:
                        self.head = self.tail = None
                        return
                    self.head = self.head.next
                    curr.next = None
                    curr = None
                    return
                elif curr == self.tail:
                    self.tail = prev
                    self.tail.next = None
                    curr = None
                    return
                else:
                    prev.next = curr.next
                    curr.next = None
                    curr = None
                    return
            prev = curr
            curr = curr.next
            j += 1

    def __str__(self):
        curr = self.head
        res = ""
        while curr:
            res = res + str(curr.val) + "->"
            curr = curr.next
        return res
    
if __name__ == "__main__":
    print("=== Testing Singly Linked List ===\n")
    
    # Test 1: Basic insertions
    print("Test 1: Basic insertions")
    llist = LinkedList()
    llist.insertBack(1)
    llist.insertBack(2)
    llist.insertBack(3)
    llist.insertFront(0)
    print(f"List: {llist}")  # Expected: 0->1->2->3->
    print(f"Size: {llist.size}")  # Expected: 4
    print()
    
    # Test 2: Get elements
    print("Test 2: Get elements")
    print(f"Get index 0: {llist.get(0)}")  # Expected: 0
    print(f"Get index 1: {llist.get(1)}")  # Expected: 1
    print(f"Get index 3: {llist.get(3)}")  # Expected: 3
    print()
    
    # Test 3: Remove elements
    print("Test 3: Remove elements")
    llist.remove(1)  # Remove element at index 1 (value 1)
    print(f"After removing index 1: {llist}")  # Expected: 0->2->3->
    print(f"Size: {llist.size}")  # Expected: 3
    
    llist.remove(0)  # Remove first element
    print(f"After removing first: {llist}")  # Expected: 2->3->
    print(f"Size: {llist.size}")  # Expected: 2
    
    llist.remove(1)  # Remove last element
    print(f"After removing last: {llist}")  # Expected: 2->
    print(f"Size: {llist.size}")  # Expected: 1
    print()
    
    # Test 4: Edge cases - single element
    print("Test 4: Single element operations")
    single_list = LinkedList()
    single_list.insertBack(42)
    print(f"Single element list: {single_list}")  # Expected: 42->
    print(f"Get element: {single_list.get(0)}")  # Expected: 42
    single_list.remove(0)
    print(f"After removing single element: {single_list}")  # Expected: (empty)
    print(f"Size: {single_list.size}")  # Expected: 0
    print()
    
    # Test 5: Empty list operations
    print("Test 5: Empty list operations")
    empty_list = LinkedList()
    print(f"Empty list: {empty_list}")
    print(f"Size: {empty_list.size}")  # Expected: 0
    
    # Add to empty list
    empty_list.insertFront(100)
    print(f"After insertFront to empty: {empty_list}")  # Expected: 100->
    print()
    
    # Test 6: Mixed operations
    print("Test 6: Mixed operations")
    mixed_list = LinkedList()
    mixed_list.insertBack(10)
    mixed_list.insertFront(5)
    mixed_list.insertBack(15)
    mixed_list.insertFront(1)
    print(f"Mixed operations result: {mixed_list}")  # Expected: 1->5->10->15->
    print(f"Size: {mixed_list.size}")  # Expected: 4
    print()
    
    # Test 7: Error handling
    print("Test 7: Error handling")
    try:
        mixed_list.get(10)  # Should raise error
    except ValueError as e:
        print(f"Get out of bounds error: {e}")
    
    try:
        mixed_list.remove(10)  # Should raise error
    except ValueError as e:
        print(f"Remove out of bounds error: {e}")
    print()
    
    # Test 8: Large list operations
    print("Test 8: Large list operations")
    large_list = LinkedList()
    for i in range(10):
        large_list.insertBack(i)
    
    print(f"Large list: {large_list}")
    print(f"Size: {large_list.size}")  # Expected: 10
    print(f"Get middle element (index 5): {large_list.get(5)}")  # Expected: 5
    
    # Remove some elements
    large_list.remove(0)  # Remove first
    large_list.remove(8)  # Remove last (now at index 8)
    large_list.remove(4)  # Remove middle
    print(f"After removals: {large_list}")
    print(f"Size: {large_list.size}")  # Expected: 7
    
    print("\n=== All tests completed ===")


