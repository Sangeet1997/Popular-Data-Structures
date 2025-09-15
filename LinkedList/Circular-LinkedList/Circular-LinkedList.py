class Node:
    def __init__(self, val = 0):
        self.val = 0
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def _empty_list(self):
        if self.size == 0:
            raise ValueError("Empty Linked List")
        return
    
    def insert_start(self, val):
        self.size += 1
        if self.size == 0:
            self.head = Node(val)
            self.tail = self.head
            self.head.next = self.tail
            return

        temp = Node(val)
        self.tail.next = temp
        temp.next = self.head
        self.head = temp

    def insert_end(self, val):
        self.size += 1
        if self.size == 0:
            self.head = Node(val)
            self.tail = self.head
            self.head.next = self.tail
            return
        
        temp = Node(val)
        self.tail.next = temp
        temp.next = self.head
        self.tail = temp

    def delete_start(self):
        self._empty_list()
        val = self.head.val
        self.size -= 1

        if self.size == 1:
            self.head = None
            self.tail = None
            return val

        self.head = self.head.next
        self.tail.next = self.head
        return val

    def delete_end(self):
        self._empty_list()
        val = self.tail.val
        self.size -= 1

        if self.size == 1:
            self.head = None
            self.tail = None
            return val
        
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next

        self.tail = curr
        self.tail.next = self.head
        return val
    
    def search(self, val):
        
        curr = self.head
        