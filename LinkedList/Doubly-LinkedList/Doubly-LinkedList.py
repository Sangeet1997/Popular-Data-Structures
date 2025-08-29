class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        self.prev = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addFront(self, val):
        self.size += 1
        if self.head == None:
            self.head = self.tail = Node(val)
            return
        temp = Node(val)
        self.head.prev = temp
        temp.next = self.head
        self.head = temp
    
    def addBack(self, val):
        self.size += 1
        if self.head == None:
            self.head = self.tail = Node(val)
            return
        temp = Node(val)
        self.tail.next = temp
        temp.prev = self.tail
        self.tail = temp

    def deleteFront(self):
        if self.size == 0:
            raise ValueError("Linked List is empty")
        if self.size == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            temp = None
        self.size -= 1
    
    def deleteBack(self):
        if self.size == 0:
            raise ValueError("Linked List is empty.")
        if self.size == 1:
            self.head = self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            temp = None
        self.size -= 1

    def __getitem__(self, i):
        if i >= self.size:
            raise ValueError("Index out of bounds.")
        j = 0
        curr = self.head
        while curr:
            if j == i:
                return curr.val
            j += 1
            curr = curr.next
    
    def __setitem__(self, i, new_val):
        if i >= self.size:
            raise ValueError("Index out of bounds.")
        j = 0
        curr = self.head
        while curr:
            if j == i:
                curr.val = new_val
                return
            j += 1
            curr = curr.next
    
    def __str__(self):
        if self.size == 0:
            return "None"
        res = "None<-"
        curr = self.head
        while True:
            if curr.next:
                res = res + str(curr.val) + "<->"
            else:
                res = res + str(curr.val)
                break
        res = res + "->None"
        return res
    
    def __len__(self):
        return self.size

    def __iter__(self):
        self.iterator = self.head
        return self
    
    def __next__(self):
        if not self.iterator:
            raise StopIteration
        else:
            val = self.iterator.val
            self.iterator = self.iterator.next
            return val
    
    
        

    
