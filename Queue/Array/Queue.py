class Queue:
    def __init__(self):
        self.arr = []
        self.index = 0
    
    def __len__(self):
        return len(self.arr) - self.index
    
    def add(self, val):
        self.arr.append(val)

    def pop(self):
        if len(self.arr) == self.index:
            raise ValueError("Queue empty")
        res = self.arr[self.index]
        self.index += 1
        return res
        
    def __getitem__(self, i):
        new_i = self.index + i
        return self.arr[new_i]
    
    def __setitem__(self, i, val):
        new_i = self.index + i
        self.arr[new_i] = val
    
    def __iter__(self):
        return self.QueueIterator(self)
    
    class QueueIterator:
        def __init__(self, queue):
            self.queue = queue
            self.index = queue.index

        def __next__(self):
            if self.index < len(self.queue.arr):
                temp = self.queue.arr[self.index]
                self.index += 1
                return temp
            else:
                raise StopIteration
            
if __name__ == "__main__":

    q = Queue()

    q.add(1)
    q.add(2)
    q.add(3)
    q.add(4)
    q.add(5)
    q.add(6)
    q.add(7)
    print(q.pop())
    print(q.pop())
    print()
    for ele in q:
        print(ele)
    print(len(q))
    