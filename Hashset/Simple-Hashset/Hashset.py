class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

class Hashset:
    """Creating a hashset of 1000 indexes"""
    def __init__(self):
        self.arr = [None] * 1000
        
    def calculate_hash(self, val):
        hash = val%1000
        return hash
    
    def add(self, val):
        hash = self.calculate_hash(val)
        if self.arr[hash]:
            curr = self.arr[hash]
            while curr.next:
                if curr.val == val:
                    print("Element already in hashset.")
                    return
                curr = curr.next
            if curr.val == val:
                print("Element already in hashset.")
                return
            curr.next = LinkedList(val)
        else:
            self.arr[hash] = LinkedList(val)
    
    def delete(self, val):
        hash = self.calculate_hash(val)

        if self.arr[hash]:
            curr = self.arr[hash]
            if curr.val == val:
                self.arr[hash] = self.arr[hash].next
                curr = None
                return 
            else:
                while curr and curr.next:
                    if curr.next.val == val:
                        curr.next = curr.next.next
                        return
                    curr = curr.next
        print("Value not present in Hashset...")

    def show(self):
        res = []
        for ele in self.arr:
            if ele:
                curr = ele
                while curr:
                    res.append(curr.val)
                    curr = curr.next
        print(res)

if __name__ == "__main__":
    h = Hashset()
    print("add, delete, show, exit")
    while True:
        query = input("->")
        arr = query.split(" ")
        if arr[0] == "add":
            h.add(int(arr[1]))
        elif arr[0] == "delete":
            h.delete(int(arr[1]))
        elif arr[0] == "show":
            h.show()
        elif arr[0] == "exit":
            break


            
        