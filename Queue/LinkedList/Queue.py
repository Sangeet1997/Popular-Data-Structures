class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, val):
        if self.size == 0:
            self.head = self.tail = Node(val)
            self.size += 1
            return
        
        temp = Node(val)
        self.tail.next = temp
        self.tail = temp
        self.size += 1
        
    def pop(self):
        if self.size == 0:
            raise ValueError("Empty Queue.")
        
        if self.size == 1:
            val = self.head.val
            self.head = self.tail = None
            self.size -= 1
            return val

        val = self.head.val
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.size -= 1
        return val
    
    def __len__(self):
        return self.size
    
    def peek(self):
        if not self.size:
            raise ValueError("Empty Queue.")
        return self.head.val
    
    def __getitem__(self, index):
        if index >= self.size:
            raise ValueError("Index out of bounds.")
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val
    
    def __setitem__(self, index, val):
        if index >= self.size:
            raise ValueError("Index out of bounds.")
        curr = self.head
        for i in range(index):
            curr = curr.next
        curr.val = val

    def __iter__(self):
        return self.QueueIterator(self)
        
    class QueueIterator:
        def __init__(self, queue):
            self.queue = queue
            self.curr = queue.head

        def __next__(self):
            if not self.curr:
                raise StopIteration
            
            val = self.curr.val
            self.curr = self.curr.next
            return val
        
if __name__ == "__main__":
    q = Queue()

    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    q.push(6)
    q.push(7)
    q.push(8)
    q[6] = 7000
    q[7] = 8000
    for ele in q:
        print(ele, end = ",")
    print()

    print(q.pop())
    print(q.pop())
    
    for ele in q:
        print(ele, end = ",")
    print()

    for ele in q:
        print(ele, end = ",")
    print()
