"""

79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        m, n, l = len(board), len(board[0]), len(word)
        if m * n < l:
            return False

        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j, visited):
                    return True
        return False

    def dfs(self, board, word, x, y, visited):

        if not word:
            return True

        if x < 0 or y < 0 or x == len(board) or y == len(board[0]) or board[x][y] != word[0]:
            return False

        visited[x][y] = True

        res = self.dfs(board, word[1:], x + 1, y, visited) or \
              self.dfs(board, word[1:], x - 1, y, visited) or \
              self.dfs(board, word[1:], x, y + 1, visited) or \
              self.dfs(board, word[1:], x, y - 1, visited)

        # if res is true, whether to restore does not matter
        visited[x][y] = False
        return res


if __name__ == '__main__':
    sol = Solution()
    method = sol.exist

    cases = [

        (method, ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"), True),
        (method, ([["a","b"]],"ba"), True),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))
