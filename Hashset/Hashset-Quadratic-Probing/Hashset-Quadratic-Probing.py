class Hashset():
    def __init__(self):
        self.arr = [None]*10
        self.DELETED = "DELETED"
        self.count = 0 # Number of elements 

    
    def hash(self, val, i):
        hash_value = (val*31 + i**2) % len(self.arr) # Less clusturing with 31
        return hash_value
    
    def add(self,val):
        i = 0
        if self.count/len(self.arr) > 0.6: # load factor monitoring
            self.resize_set()
        while True:
            print("hash attempt:",i)
            hash_val = self.hash(val, i)
            i += 1
            if self.arr[hash_val] == val:
                print("Element already present at pos:", hash_val)
                break
            if self.arr[hash_val] == None or self.arr[hash_val] == self.DELETED:
                self.arr[hash_val] = val
                self.count += 1 # increment number of elements
                break
    
    def resize_set(self):
        backup_arr = []
        for ele in self.arr:
            if ele != None and ele != self.DELETED:
                backup_arr.append(ele)
        
        l = len(self.arr) # current length
        self.arr = [None] * (l*2)
        self.count = 0 # reset count
        print("Resizing Hashset length to:",l * 2)

        for ele in backup_arr:
            self.add(ele)


    def find_index(self, val):
        i = 0
        while True:
            print("hash attempt:",i)
            hash_val = self.hash(val, i)
            i += 1
            if self.arr[hash_val] == val or self.arr[hash_val] == None:
                return hash_val
            else:
                continue

    def get(self, val):
        i = self.find_index(val)
        if self.arr[i] == None:
            return False
        else:
            return True
    
    def delete(self, val):
        i = self.find_index(val)
        if self.arr[i]:
            self.arr[i] = self.DELETED
            self.count -= 1 # decrement number of elements
        else:
            print("Element Not present")
    
    def show(self):
        print(self.arr)

if __name__ == "__main__":
    print("Operations: add, delete, get, show, exit")
    hset = Hashset()
    while True:
        query = input(">>").split(" ")
        x = query[0]
        y = 0
        if len(query) > 1:
            y = int(query[1])

        if x == "add":
            hset.add(y)

        elif x == "delete":
            hset.delete(y)
        
        elif x == "show":
            hset.show()

        elif x == "get":
            print(hset.get(y))
        
        elif x == "exit":
            break

            
    
    