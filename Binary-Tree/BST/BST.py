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
        self.res = ""
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.res = self.res + str(root.val) + "->"
            dfs(root.right)
        dfs(self.root)
        return self.res
    
    def preorder(self):
        self.res = ""
        def dfs(root):
            if not root:
                return
            self.res = self.res + str(root.val) + "->"
            dfs(root.left)
            dfs(root.right)
        dfs(self.root)
        return self.res
    
    def postorder(self):
        self.res = ""
        def dfs(root):
            if not root:
                return
            self.res = self.res + str(root.val) + "->"
            dfs(root.left)
            dfs(root.right)
        dfs(self.root)
        return self.res
       

    
if __name__ == "__main__":
    print("Hello World")