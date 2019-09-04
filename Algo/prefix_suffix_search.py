"""

745.
Hard

"""

from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix = {}
        self.suffix = {}
        self.build_trie(words)

    def f(self, prefix: str, suffix: str) -> int:
        pw = self.search_prefix(prefix)
        sw = self.search_suffix(suffix)

        if not pw or not sw:
            return -1
        else:
            max_weight = -1
            for k, w in pw.items():
                if k in sw:
                    max_weight = max(max_weight, pw[k])
            return max_weight

    def build_trie(self, words):
        for i, word in enumerate(words):
            self.insert(word, i)

    def insert(self, word, weight):
        p = self.prefix
        for w in word:
            if w not in p:
                p[w] = {}
            p = p[w]
        p['end'] = weight

        p = self.suffix
        for w in reversed(word):
            if w not in p:
                p[w] = {}
            p = p[w]
        p['end'] = weight

    def search_suffix(self, suffix):
        weights = {}
        p = self.suffix
        if not suffix:
            self.visit(p, suffix, weights, prefix=False)
            return weights

        for w in reversed(suffix):
            if w in p:
                p = p[w]
            else:
                return {}

        self.visit(p, suffix, weights, prefix=False)
        return weights

    def search_prefix(self, prefix):
        weights = {}
        p = self.prefix
        if not prefix:
            self.visit(p, prefix, weights, prefix=True)
            return weights

        for w in prefix:
            if w in p:
                p = p[w]
            else:
                return {}

        self.visit(p, prefix, weights, prefix=True)
        return weights

    def visit(self, root, curr, nodes, prefix=True):
        if "end" in root:
            nodes[curr] = root['end']
            return

        for k in root.keys():
            if prefix:
                self.visit(root[k], curr + k, nodes, prefix)
            else:
                self.visit(root[k], k + curr, nodes, prefix)

        return nodes


if __name__ == '__main__':
    words = ['pop', 'apple']
    wf = WordFilter(words)
    print(wf.f('', ''))
    print(wf.f('', 'p'))
    print(wf.f('', 'gp'))
    print(wf.f('', 'op'))
    print(wf.f('a', 'e'))