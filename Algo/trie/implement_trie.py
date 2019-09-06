"""


"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False


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

        p = self.root
        for w in word:
            if w not in p.children:
                p.children[w] = TrieNode()
            p = p.children[w]
        p.endofword = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        p = self.root
        for w in word:
            if w not in p.children:
                return False
            else:
                p = p.children[w]
        if p.endofword:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        p = self.root
        for w in prefix:
            if w not in p.children:
                return False
            else:
                p = p.children[w]
        return True