class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, s):
        curr = self.root
        for ch in s:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                new_node = TrieNode()
                curr.children[ch] = new_node
                curr = curr.children[ch]
        curr.end = True
        return
    
    def searchWord(self, s):
        curr = self.root
        for ch in s:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False
        return curr.end

    def startsWith(self, s):
        curr = self.root
        for ch in s:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False
        return True
    
if __name__=="__main__":
    print("=== Testing Trie ===\n")
    
    trie = Trie()
    
    # Test 1: Basic word insertion and search
    print("Test 1: Basic operations")
    trie.addWord("apple")
    trie.addWord("app")
    trie.addWord("application")
    
    print(f"Search 'apple': {trie.searchWord('apple')}")  # True
    print(f"Search 'app': {trie.searchWord('app')}")      # True
    print(f"Search 'appl': {trie.searchWord('appl')}")    # False
    print(f"Search 'orange': {trie.searchWord('orange')}")# False
    print()
    
    # Test 2: Prefix checking
    print("Test 2: Prefix checking")
    print(f"Starts with 'app': {trie.startsWith('app')}")         # True
    print(f"Starts with 'appl': {trie.startsWith('appl')}")       # True
    print(f"Starts with 'apple': {trie.startsWith('apple')}")     # True
    print(f"Starts with 'applic': {trie.startsWith('applic')}")   # True
    print(f"Starts with 'orange': {trie.startsWith('orange')}")   # False
    print(f"Starts with 'xyz': {trie.startsWith('xyz')}")         # False
    print()
    
    # Test 3: Empty string and single character
    print("Test 3: Edge cases")
    trie.addWord("")
    trie.addWord("a")
    print(f"Search empty string: {trie.searchWord('')}")    # True
    print(f"Search 'a': {trie.searchWord('a')}")            # True
    print(f"Starts with empty: {trie.startsWith('')}")      # True
    print(f"Starts with 'a': {trie.startsWith('a')}")       # True
    print()
    
    # Test 4: Overlapping words
    print("Test 4: Overlapping words")
    trie.addWord("cat")
    trie.addWord("cats")
    trie.addWord("category")
    
    print(f"Search 'cat': {trie.searchWord('cat')}")          # True
    print(f"Search 'cats': {trie.searchWord('cats')}")        # True
    print(f"Search 'category': {trie.searchWord('category')}")# True
    print(f"Search 'ca': {trie.searchWord('ca')}")            # False
    print(f"Starts with 'cat': {trie.startsWith('cat')}")     # True
    print()
    
    # Test 5: Case sensitivity
    print("Test 5: Case sensitivity")
    trie.addWord("Hello")
    print(f"Search 'Hello': {trie.searchWord('Hello')}")      # True
    print(f"Search 'hello': {trie.searchWord('hello')}")      # False
    print(f"Starts with 'Hel': {trie.startsWith('Hel')}")     # True
    print(f"Starts with 'hel': {trie.startsWith('hel')}")     # False
    print()
    
    # Test 6: Numbers and special characters
    print("Test 6: Numbers and special characters")
    trie.addWord("123")
    trie.addWord("test-word")
    trie.addWord("user@email.com")
    
    print(f"Search '123': {trie.searchWord('123')}")              # True
    print(f"Search 'test-word': {trie.searchWord('test-word')}")  # True
    print(f"Search 'user@email.com': {trie.searchWord('user@email.com')}")  # True
    print(f"Starts with 'test-': {trie.startsWith('test-')}")     # True
    print()
    
    print("=== All tests completed ===")
