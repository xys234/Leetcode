"""

980. Unique Paths III
Hard

"""

from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        unvisited, origin, dest = 0, None, None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    unvisited += 1
                elif grid[i][j] == 1:
                    origin = (i, j)
                else:
                    dest = (i, j)

        def dfs(i, j, unvisited, ans):
            if i == dest[0] and j == dest[1]:
                if unvisited == 0:
                    ans[0] += 1
                return

            if i + 1 < m and grid[i+1][j] not in {3, -1}:
                temp = grid[i+1][j]
                if temp != 2:
                    grid[i+1][j] = 3
                    dfs(i+1, j, unvisited-1, ans)
                    grid[i+1][j] = temp
                else:
                    dfs(i + 1, j, unvisited - 1, ans)

            if i >= 1 and grid[i-1][j] not in {3, -1}:
                temp = grid[i - 1][j]
                if temp != 2:
                    grid[i - 1][j] = 3
                    dfs(i - 1, j, unvisited - 1, ans)
                    grid[i - 1][j] = temp
                else:
                    dfs(i - 1, j, unvisited - 1, ans)

            if j + 1 < n and grid[i][j+1] not in {3, -1}:
                temp = grid[i][j+1]
                if temp != 2:
                    grid[i][j+1] = 3
                    dfs(i, j+1, unvisited - 1, ans)
                    grid[i][j+1] = temp
                else:
                    dfs(i, j+1, unvisited - 1, ans)

            if j >= 1 and grid[i][j-1] not in {3, -1}:
                temp = grid[i][j-1]
                if temp != 2:
                    grid[i][j-1] = 3
                    dfs(i, j+1, unvisited - 1, ans)
                    grid[i][j-1] = temp
                else:
                    dfs(i, j+1, unvisited - 1, ans)