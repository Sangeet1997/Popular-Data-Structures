"""
List Implementation

     0        1   2        3   4    5     6
0    1 2      3 4 5 6      7 8 9 10 11 12 13 14

0 index as root
left child for any index = index*2 + 1
right child for any index = index*2 + 2
parent = (child - 1)//2
check above for explanation
"""

class Heap:
    def __init__(self, arr = None):
        if not arr:
            self.arr = []
            return
        self.arr = arr[::]
        self._heapify()
        
    def _heapify(self):
        """Build heap from bottom up"""
        # Start from last non-leaf node
        start = (len(self.arr) - 2) // 2
        for i in range(start, -1, -1):
            self._downshift(i)

    def _downshift(self, i):
        left = float('inf') # basically None
        right = float('inf') 
        curr = self.arr[i]

        if (i*2 + 1) < len(self.arr):
            left = self.arr[i*2 + 1]
        
        if (i*2 + 2) < len(self.arr):
            right = self.arr[i*2 + 2]
        
        if left == float('inf')  and right == float('inf'):
            return
        
        if left <= right:
            if left < curr:
                self.arr[i] = left
                self.arr[i*2 + 1] = curr
                self._downshift(i*2 + 1)
        
        else:
            if right < curr:
                self.arr[i] = right
                self.arr[i*2 + 2] = curr
                self._downshift(i*2 + 2)

    def _upshift(self, i):
        if (i - 1)//2 < 0:
            return
        
        parent = self.arr[(i - 1)//2]
        curr = self.arr[i]
        
        if curr < parent:
            self.arr[i] = parent
            self.arr[(i-1)//2] = curr
            self._upshift((i-1)//2)
        
    def push(self, ele):
        if not self.arr: 
            self.arr = [ele]
            return
        
        self.arr.append(ele)
        index = len(self.arr) - 1
        self._upshift(index)
    
    def pop(self):
        if not self.arr:
            return None
        temp = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        if self.arr:
            self._downshift(0)
        return temp
    
    def peek(self):
        if not self.arr:
            return None
        return self.arr[0]

import time
import random
import heapq

if __name__ == "__main__":
    
    start_time = time.perf_counter()
    arr = []
    for i in range(1000000): # array of 1 million random numbers
        arr.append(random.randint(0,1000))
    end_time = time.perf_counter()
    print(f"Time taken to generate 1M numbers:\t\t{(end_time - start_time) * 1000:.4f} ms")
    
    # initilizing with arr
    start_time = time.perf_counter()
    heap1 = Heap(arr)
    end_time = time.perf_counter()
    print(f"Time taken to initialize heap1 with array:\t{(end_time - start_time) * 1000:.4f} ms")

    # adding all elements with push
    start_time = time.perf_counter()
    heap2 = Heap()
    for ele in arr:
        heap2.push(ele)
    end_time = time.perf_counter()
    print(f"Time taken to build heap2 with push operations:\t{(end_time - start_time) * 1000:.4f} ms")

    # heap3 with heapq heapify
    heap3 = arr[::]
    start_time = time.perf_counter()
    heapq.heapify(heap3)
    end_time = time.perf_counter()
    print(f"Time taken to build heap3 with heapq heapify:\t{(end_time - start_time) * 1000:.4f} ms")

    # heap3 with heapq heappush
    heap4 = []
    start_time = time.perf_counter()
    for ele in arr:
        heapq.heappush(heap4,ele)
    end_time = time.perf_counter()
    print(f"Time taken to build heap4 with heapq push:\t{(end_time - start_time) * 1000:.4f} ms")

    #poping all elements from heap1
    start_time = time.perf_counter()
    while heap1.peek() != None:
        heap1.pop()
    end_time = time.perf_counter()
    print(f"Time taken to pop all elements from heap1:\t{(end_time - start_time) * 1000:.4f} ms")
    
    #poping all elements from heap2
    start_time = time.perf_counter()
    while heap2.peek() != None:
        heap2.pop()
    end_time = time.perf_counter()
    print(f"Time taken to pop all elements from heap2:\t{(end_time - start_time) * 1000:.4f} ms")

    #poping all elements from heap3
    start_time = time.perf_counter()
    while heap3:
        heapq.heappop(heap3)
    end_time = time.perf_counter()
    print(f"Time taken to pop all elements from heap3:\t{(end_time - start_time) * 1000:.4f} ms")
    
    #poping all elements from heap4
    start_time = time.perf_counter()
    while heap4:
        heapq.heappop(heap4)
    end_time = time.perf_counter()
    print(f"Time taken to pop all elements from heap4:\t{(end_time - start_time) * 1000:.4f} ms")
    pass