class TrieNode:
    def __init__(self, end=False):
        self.alpha = [None] * 26
        self.end = end

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            w_ascii = ord(w) - 97
            if curr.alpha[w_ascii] is None:
                curr.alpha[w_ascii] = TrieNode()
            curr = curr.alpha[w_ascii]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            w_ascii = ord(w) - 97
            if curr.alpha[w_ascii] is None:
                return False
            curr = curr.alpha[w_ascii]

        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for p in prefix:
            p_ascii = ord(p) - 97
            if curr.alpha[p_ascii] is None:
                return False
            curr = curr.alpha[p_ascii]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
