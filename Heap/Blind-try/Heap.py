
class Node:
    def __init__(self, val = 0):
        self.val = 0
        self.parent = None
        self.left = None
        self.right = None

class Heap:
    def __init__(self, arr = []):
        self.root = None
        self.level = defaultdict(list)

        if not arr:
            return
        
        self.root = None(arr[0])
        q = [self.root, None]
        i = 0
        level_count = 0
        for ele in arr[1:]:
            curr = q[i]

            if curr == None:
                i += 1
                q.append(None)
                curr = q[i]
                level_count += 1

            if not curr.left:
                curr.left = Node(ele)
                q.append(curr.left)
                self.level[level_count].append(curr.left)

            else:
                curr.right = Node(ele)
                q.append(curr.right)
                self.level[level_count].append(curr.right)
                i += 1
        
        level_count -= 1 # checking from 2nd last level

        for i in range(level_count, -1, -1):
            for node in self.level[i]:
                self._downshift(node)
        
                
    def _downshift(self, node):
        if not node.left and not node.right:
            return
        if node.left and node.right:
            if node.val <= node.left.val and node.val <= node.right.val:
                return
            else:
                if node.left.val <= node.right.val:
                    temp = node.val
                    node.val = node.left.val
                    node.left.val = temp
                    self._downshift(node.left)
                else:
                    temp = node.val
                    node.val = node.right.val
                    node.right.val = temp
                    self._downshift(node.right)
        if node.left:
            if node.val <= node.left.val:
                return
            else:
                temp = node.val
                node.val = node.left.val
                node.left.val = temp
                self._downshift(node.left)
        if node.right:
            if node.val <= node.right.val:
                return
            else:
                temp = node.val
                node.val = node.right.val
                node.right.val = temp
                self._downshift(node.right)
            

            

        