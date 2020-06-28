class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            if c in curr.children_letter:
                curr = curr.get_child(c)
            else:
                new_node = TrieNode(c)
                curr.add_child(new_node)
                curr = new_node
        curr.set_is_word(True)        
                
            
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            if c in curr.children_letter:
                curr = curr.get_child(c)
            else:
                return False
        
        return curr.is_word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            if c in curr.children_letter:
                curr = curr.get_child(c)
            else:
                return False
        return curr.is_word or len(curr.children_letter) > 0
        
class TrieNode:
    
    def __init__(self, l=None):
        self._is_word = False
        self._children = {}
        self._letter = l
    
    @property    
    def is_word(self):
        return self._is_word
    
    @property
    def children_letter(self):
        return list(self._children.keys())
    
    @property
    def letter(self):
        return self._letter
    
    def add_child(self, c):
        self._children[c.letter] = c
        
    def get_child(self, c):
        return self._children.get(c, None)
        
    def set_is_word(self, word):
        self._is_word = word
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)