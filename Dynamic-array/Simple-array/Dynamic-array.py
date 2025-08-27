class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity
    
    def append(self, val):
        if self.size == self.capacity:
            self._resize()
        self.arr[self.size] = val
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise ValueError("Empty array")
        x = self.arr[self.size - 1]
        self.arr[self.size - 1] = 0
        self.size -= 1
        return x
    
    def _resize(self): # only used internally
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity
        
        for i,ele in enumerate(self.arr):
            new_arr[i] = ele

        self.arr = new_arr

    def __getitem__(self, i):
        if i >= self.size:
            raise ValueError("Index out of bounds.")
        return self.arr[i]
    
    def __setitem__(self, i, val):
        if i >= self.size:
            raise ValueError("Index out of bounds.")
        self.arr[i] = val

    def __str__(self):
        res = "["
        for i in range(0,self.size):
            if i == self.size - 1: # for last element
                res = res + str(self.arr[i]) + "]"
            else:
                res = res + str(self.arr[i]) + ","
        return res

    def __len__(self):
        return self.size
    
    def get_capacity(self):
        return self.capacity
    
    def __iter__(self): # used for iteration in for 
        self.iterator = 0 # initalize iterator
        return self # tells python this object itself is the iterator
    
    # you can also create a separate class just for the iterator object
    # def __iter__(self):
    # # Create a separate iterator class or use generator
    #     return ArrayListIterator(self)
    #
    # class ArrayListIterator:
    #     def __init__(self, arraylist):
    #         self.arraylist = arraylist
    #         self.index = 0
    #
    #     def __next__(self):
    #         if self.index < self.arraylist.size:
    #             val = self.arraylist.arr[self.index]
    #             self.index += 1
    #             return val
    #         else:
    #             raise StopIteration

    def __next__(self): # called during iteration
        if self.iterator < self.size:
            val = self.arr[self.iterator]
            self.iterator += 1
            return val
        else:
            raise StopIteration
        
if __name__ =="__main__":
    arr = ArrayList(5)

    arr.append(0)
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print(arr[2])
    print(arr)
    print(len(arr))
    print(arr.get_capacity())
    arr.append(459)
    print(arr)
    arr[4] = 4789
    arr.append(3232)
    print(arr[5])
    print(arr)
    print(len(arr))
    print(arr.get_capacity())

    print()
    for ele in arr:
        print(ele)
    
    print()
    for ele in arr:
        print(ele)