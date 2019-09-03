"""

211.

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

        return self.search_helper(self.root, word)

    def search_helper(self, root, word):
        if root.endofword and not word:
            return True

        p = root
        for i, w in enumerate(word):
            if w == '.':
                for key in p.children.keys():
                    p2 = p.children[key]
                    if self.search_helper(p2, word[1:]):
                        return True
            else:
                if w in p.children:
                    return self.search_helper(p.children[w], word[1:])
                else:
                    return False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """

        self.trie.insert(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        return self.trie.search(word)


class WordDictionary2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordMap = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        currentMap = self.wordMap
        for c in word:
            if c not in currentMap:
                currentMap[c] = {}
            currentMap = currentMap[c]
        currentMap["end"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.searchRecursive(word, self.wordMap)

    def searchRecursive(self, word: str, startingMap: dict) -> bool:
        currentWordmap = startingMap
        for i in range(len(word)):
            if word[i] == ".":
                for c in currentWordmap:
                    if c != "end":
                        if self.searchRecursive(word[i + 1:], currentWordmap[c]):
                            return True
                return False
            else:
                if word[i] not in currentWordmap:
                    return False
                currentWordmap = currentWordmap[word[i]]
        return "end" in currentWordmap


if __name__ == '__main__':
    wd = WordDictionary2()
    wd.addWord('bad')
    wd.addWord('dad')
    wd.addWord('mad')
    print(wd.search('pad'))
    print(wd.search('bad'))
    print(wd.search('.ad'))
    print(wd.search('b..'))