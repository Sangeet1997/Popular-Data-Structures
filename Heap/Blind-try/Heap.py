from collections import defaultdict

class Node:
    def __init__(self, val = 0):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

class Heap:
    def __init__(self, arr = []):
        self.root = None
        self.level = defaultdict(list)
        self.max_level = 0

        if not arr:
            return
        
        self.root = Node(arr[0])
        q = [self.root, None]
        self.level[0].append(self.root)
        i = 0
        level_count = 1
        for ele in arr[1:]:
            curr = q[i]

            if curr == None:
                i += 1
                q.append(None)
                curr = q[i]
                level_count += 1

            if not curr.left:
                curr.left = Node(ele)
                curr.left.parent = curr
                q.append(curr.left)
                self.level[level_count].append(curr.left)

            else:
                curr.right = Node(ele)
                curr.right.parent = curr
                q.append(curr.right)
                self.level[level_count].append(curr.right)
                i += 1

        # print(self._traverse(self.root)) # debugging step

        self.max_level = level_count # updating max level
        level_count -= 1 # checking from 2nd last level

        for i in range(level_count, -1, -1):
            for node in self.level[i]:
                self._downshift(node)
        
        # print(self._traverse(self.root)) # debugging step
        
                
    def _downshift(self, node):
        if not node.left and not node.right:
            return
        if node.left and node.right:
            if node.val <= node.left.val and node.val <= node.right.val:
                return
            else:
                smaller = None
                if node.left.val <= node.right.val:
                    smaller = node.left
                else:
                    smaller = node.right
                temp = node.val
                node.val = smaller.val
                smaller.val = temp
                self._downshift(smaller)
                    
        child_node = None
        if node.left:
            child_node = node.left
        else:
            child_node = node.right
        
        if node.val <= child_node.val:
            return
        
        temp = node.val
        node.val = child_node.val
        child_node.val = temp
        self._downshift(child_node)
        

    def _traverse(self, node):
        
        q = [node]
        i = 0
        res = []

        while i < len(q):
            ele = q[i]
            res.append(ele.val)
            i += 1
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)
        
        return res
            

    def pop(self):
        if self.root == None:
            # print(self.max_level) # debugging step
            return "Empty Heap" # for testing, -> replace with raise IndexError
        
        last_node = self.level[self.max_level].pop()
        last_val = last_node.val

        if not last_node.parent: # root or last element left
            self.root = None
            return last_val
        
        if last_node.parent.left == last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None

        if len(self.level[self.max_level]) == 0: # edge case to decrease max level
            self.max_level -= 1

        res = self.root.val
        self.root.val = last_val
        self._downshift(self.root)
        return res
    
    def push(self, val):

        if self.root == None: # empty heap
            self.root = Node(val)
            self.level[0].append(self.root)
            return

        parent_level = self.max_level - 1
        empty_index = len(self.level[self.max_level]) # empty index at max level
        temp = Node(val)
        if empty_index == 2 ** (self.max_level): # level full, go to next level
            self.max_level += 1 # increment max level
            parent_level = self.max_level - 1
            parent_node = self.level[parent_level][0] # first(and all) parents are empty in new level
            parent_node.left = temp
            temp.parent = parent_node
        
        else:
            parent_index = empty_index // 2
            parent_node = self.level[parent_level][parent_index]
            if empty_index % 2 == 0: # even is connected to left
                parent_node.left = temp
                temp.parent = parent_node
            else: # odd is connected to right
                parent_node.right = temp
                temp.parent = parent_node
        
        self.level[self.max_level].append(temp)
        self._upshift(temp) # very important, shifts value up the tree
    
    def _upshift(self, node):
        if not node.parent:
            return
        
        if node.val > node.parent.val:
            return
        
        temp = node.val
        node.val = node.parent.val
        node.parent.val = temp
        self._upshift(node.parent)
    
    def level_traverse(self):
        return self._traverse()
    
    def peek(self):
        if self.root:
            return self.root.val
        return None

import random
import time
import heapq

if __name__ == "__main__":

    start_time = time.perf_counter()
    arr = []
    for i in range(1000000): # array of 1 million random numbers
        arr.append(random.randint(0,1000))
    end_time = time.perf_counter()
    print(f"Time taken to generate numbers:\t\t\t{(end_time - start_time) * 1000:.4f} ms")
    
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

    #sorting arr with inbuilt function
    start_time = time.perf_counter()
    arr.sort()
    end_time = time.perf_counter()
    print(f"Time taken to sort array with built-in sort:\t{(end_time - start_time) * 1000:.4f} ms")

    # heap3 with heapq heapify
    heap3 = arr
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

    print("\n\nInbuilt implementaion is much faster because:\n1. heapq is implemented in C.\n2. heapq uses array insead of tree.")