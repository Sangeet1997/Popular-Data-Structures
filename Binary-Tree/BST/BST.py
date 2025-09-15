class Node:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, val):
        if self.size == 0:
            new_node = Node(val)
            self.root = new_node
            self.size += 1
        else:
            curr = self.root
            while curr:
                if curr.val == val:
                    print("Value already present.")
                    return
                elif val > curr.val:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(val)
                        self.size += 1
                        return # stop operation
                else:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(val)
                        self.size += 1
                        return # stop operation
    
    def search(self, val):
        if self.size == 0:
            raise ValueError("BST is empty.")
        else:
            curr = self.root
            while curr:
                if curr.val == val:
                    return True
                elif val > curr.val:
                    curr = curr.right
                elif val < curr.val:
                    curr = curr.left
        return False
    
    def find_min(self):
        if self.size == 0:
            raise ValueError("BST is empty.")
        curr = self.root
        prev = None
        while curr:
            prev = curr
            curr = curr.left
        return prev.val
    
    def find_max(self):
        if self.size == 0:
            raise ValueError("BST is empty.")
        curr = self.root
        prev = None
        while curr:
            prev = curr
            curr = curr.right
        return prev.val
    
    def _helper(self, node):
        # getting and deleting the largest element in the left subtree
        prev = node
        curr = node.left

        while curr.right:
            prev = curr
            curr = curr.right
        if prev == node:
            prev.left = None
        else: 
            prev.right = None
        return curr.val
    
    def remove(self, val):
        if self.size == 0:
            raise ValueError("BST is empty.")
        curr = self.root
        prev = None
        while curr:
            if val < curr.val:
                prev = curr
                curr = curr.left
            elif val > curr.val:
                prev = curr
                curr = curr.right
            else: # val == curr.val
                self.size -= 1
                count = 0 # child count
                if curr.left: count += 1
                if curr.right: count += 1

                # no child
                if count == 0:
                    # root node
                    if not prev:
                        self.root = None
                    else:
                        if curr.val > prev.val:
                            prev.right = None
                        else:
                            prev.left = None

                # one child
                if count == 1:
                    temp = None
                    # checking which side is the child
                    if curr.left:
                        temp = curr.left
                    else:
                        temp = curr.right
                    # root node
                    if not prev:
                        self.root = temp
                    else:
                        if curr.val > prev.val:
                            prev.right = temp
                        else:
                            prev.left = temp

                # two child
                if count == 2:
                    # Either find largest element in left subtree
                    # Or find smallest element in right subtree
                    x = self._helper(curr)
                    curr.val = x
                
                return
            
    def inorder(self):
        self.res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.res.append(root.val)
            dfs(root.right)
        dfs(self.root)
        return self.res
    
    def preorder(self):
        self.res = []
        def dfs(root):
            if not root:
                return
            self.res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(self.root)
        return self.res
    
    def postorder(self):
        self.res = ""
        def dfs(root):
            if not root:
                return
            self.res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(self.root)
        return self.res
    
    def levelorder(self):
        res = []
        i = 0
        q = [self.root]
        while i < len(q):
            ele = q[i]
            i += 1
            res.append(ele.val)
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)
        return res
    
    #list of utility/advanced functions
    def height(self):
        if not self.root:
            return 0
        h = 1
        curr = self.root
        
        q = [self.root,None]
        i = 0

        while i < len(q) - 1:
            ele = q[i]
            i += 1
            if not ele:
                q.append(None)
                h += 1
                continue
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)
        
        return h
    
    def is_balanced(self):
        self.res = True
        def dfs(root):
            if not root:
                return 0
            
            x = dfs(root.left)
            y = dfs(root.right)
            if abs(x-y) > 1:
                self.res = False
            return max(x,y) + 1
        dfs(self.root)
        return self.res
    
    def count_node(self):
        return self.size
    
    def count_leaves(self):
        self.res = 0
        def dfs(root):
            if not root: 
                return
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            if not root.left and not root.right:
                self.res += 1
        return self.res
    
    def LCA(self, val1, val2):
        curr = self.root
        if val1 > val2:
            val1, val2 = val2, val1
        while curr:
            if (curr.val > val1 and curr.val < val2) or curr.val == val1 or curr.val == val2:
                return curr.val
            if curr.val < val1:
                curr = curr.left
            else:
                curr = curr.right
    
    def predecessor(self, val):
        self.prev = None
        self.res = None

        def dfs(root, target):
            if self.res:
                return
            if not root:
                return
            dfs(root.left, target)
            if root.val == target:
                self.res = self.prev
                return
            self.prev = root
            dfs(root.right, target)
        
        if not self.res:
            raise ValueError("No Predecessor.")
        return self.res
        
    def successor(self, val):
        self.prev = None
        self.res = None
        
        def dfs(root, target):
            if not root:
                return
            if self.res:
                return
            dfs(root.left, target)
            if self.prev:
                if self.prev.val == target:
                    self.res = root
                self.prev = root
            dfs(root.right, target)

        if not self.res:
            raise ValueError("No Successor")
        return self.res
    
    def serialize(self):
        res = []
        q = [self.root]
        i = 0
        while i < len(q):
            ele = q[i]
            i += 1
            if ele:
                res.append(ele.val)
                q.append(ele.left)
                q.append(ele.right)
            else:
                res.append(None)
        return res        
    
    
    
if __name__ == "__main__":
    print("Hello World")