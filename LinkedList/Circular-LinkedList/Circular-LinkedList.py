class Node:
    def __init__(self, val = 0):
        self.val = val
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
        
        if self.size == 0:
            self.size += 1
            self.head = Node(val)
            self.tail = self.head
            self.head.next = self.tail
            return
        
        self.size += 1
        temp = Node(val)
        self.tail.next = temp
        temp.next = self.head
        self.head = temp

    def insert_end(self, val):

        if self.size == 0:
            self.size += 1
            self.head = Node(val)
            self.tail = self.head
            self.head.next = self.tail
            return
        
        self.size += 1
        temp = Node(val)
        self.tail.next = temp
        temp.next = self.head
        self.tail = temp

    def delete_start(self):
        self._empty_list()
        val = self.head.val
        
        if self.size == 1:
            self.size -= 1
            self.head = None
            self.tail = None
            return val
        
        self.size -= 1
        self.head = self.head.next
        self.tail.next = self.head
        return val

    def delete_end(self):
        self._empty_list()
        val = self.tail.val

        if self.size == 1:
            self.size -= 1
            self.head = None
            self.tail = None
            return val
        
        self.size -= 1
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next

        self.tail = curr
        self.tail.next = self.head
        return val
    
    def search(self, val):
        if self.is_empty():  # Return False instead of raising error
            return False
        curr = self.head
        check = True
        while check or curr != self.head:
            check = False
            if curr.val == val:
                return True
            curr = curr.next
        return False
    
    def __str__(self):
        if self.size == 0:
            return "None"
        curr = self.head
        res = ""
        flag = True

        while flag or curr != self.head:
            flag = False
            res += str(curr.val)
            if curr == self.head:
                res += "(head)"
            if curr == self.tail:
                res += "(tail)"
            res += "->"
            curr = curr.next
        
        res += str(curr.val)
        if curr == self.head:
            res += "(head)"
        if curr == self.tail:
            res += "(tail)"

        return res
     
    def insert_after_node(self, target, val):
        self._empty_list()
        curr = self.head
        flag = True

        while flag or curr != self.head:
            flag = False
            if curr.val == target:
                self.size += 1
                temp = Node(val)
                temp.next = curr.next
                curr.next = temp
                if temp.next == self.head:
                    self.tail = temp
                return
            curr = curr.next
        
        raise ValueError("Target node not found.")
    
    def delete_node(self, val):
        self._empty_list()
        curr = self.head
        flag = True
        target_found = False

        while flag or curr != self.head:
            flag = False
            if curr.next.val == val:
                target_found = True
                break
            curr = curr.next
        if not target_found:
            raise ValueError("Target node not found.")
        
        self.size -= 1

        if curr.next == curr:
            self.head = None
            self.tail = None
        else:
            temp = curr.next
            curr.next = temp.next
            temp.next = None
            if temp == self.head:
                self.head = curr.next
            if temp == self.tail:
                self.tail = curr
        return
    
class Utility:
    # Clear intent - Shows this is a general utility, not tied to a specific instance
    # Memory efficient - No need to instantiate the Utility class
    @staticmethod  # Operates on the passed-in list, not self.something
    def split(list1):
        if len(list1) == 1 or len(list1) == 0:
            raise ValueError("List of size 0 or 1 cannot be split")
        
        slow = list1.head
        fast = list1.head

        if len(list1) == 2:
            list2 = LinkedList()
            list2.insert_start(list1.tail.val)
            list1.delete_end()

            return [list1,list2]

        while fast != list1.tail and fast.next != list1.tail:
            fast = fast.next.next
            slow = slow.next

        head2 = slow.next
        tail2 = list1.tail

        list1.tail = slow
        list1.tail.next = list1.head

        tail2.next = head2
        list2 = LinkedList()
        list2.head = head2
        list2.tail = tail2

        list2.size = list1.size//2
        list1.size = list1.size - list2.size
        
        return [list1, list2]