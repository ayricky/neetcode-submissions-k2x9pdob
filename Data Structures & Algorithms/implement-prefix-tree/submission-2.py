class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        i = 0
        while i < len(word):
            char = word[i]
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
            if i == len(word) - 1:
                curr.is_word = True

            i += 1 

    def search(self, word: str) -> bool:
        curr = self.root

        i = 0
        while i < len(word):
            char = word[i]
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
            if i == len(word) - 1 and curr.is_word:
                return True

            i += 1
        
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        i = 0
        while i < len(prefix):
            char = prefix[i]
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
            if i == len(prefix) - 1:
                return True

            i += 1
        
        return False