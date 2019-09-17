"""

200.

Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3


"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        grid = [[s[j] for j in range(len(s))] for s in grid]
        total_island = 0

        def dfs(pos, q):

            grid[pos[0]][pos[1]] = '0'
            next_nodes = [(pos[0]+d[0], pos[1]+d[1]) for d in directions if 0 <= pos[0]+d[0] < m and
                          0 <= pos[1]+d[1] < n]

            q.extend(next_nodes)
            while q:
                top = q[0]
                q.pop(0)
                if grid[top[0]][top[1]] == '1':
                    dfs(top, q)

        # find a '1'. if none, return the number of island found
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    start_pos = (i, j)
                    dfs(start_pos, [])
                    total_island += 1

        return total_island

    def numIslands2(self, grid):
        if not grid:
            return 0

        r = len(grid)
        c = len(grid[0])

        def dfs(grid, x, y):
            grid[x][y] = "#"

            if x + 1 < r and grid[x + 1][y] == "1":
                dfs(grid, x + 1, y)
            if x - 1 >= 0 and grid[x - 1][y] == "1":
                dfs(grid, x - 1, y)
            if y + 1 < c and grid[x][y + 1] == "1":
                dfs(grid, x, y + 1)
            if y - 1 >= 0 and grid[x][y - 1] == "1":
                dfs(grid, x, y - 1)

        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    count += 1

        return count

    def numIslands3(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m > 0:
            n = len(grid[0])
        else:
            return 0

        def dfs(grid, i, j):
            if grid[i][j] != '0':
                grid[i][j] = '0'

                for direction in self.directions(grid, i, j):
                    dfs(grid, direction[0], direction[1])

        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island += 1
                    dfs(grid, i, j)
        return island

    def directions(self, grid, p, q):
        k = len(grid)
        l = len(grid[0])
        d = []

        if p + 1 < k and grid[p + 1][q] == '1':
            d.append((p + 1, q))
        if p - 1 >= 0 and grid[p - 1][q] == '1':
            d.append((p - 1, q))
        if q + 1 < l and grid[p][q + 1] == '1':
            d.append((p, q+1))
        if q - 1 >= 0 and grid[p][q - 1] == '1':
            d.append((p, q-1))
        return d


if __name__ == '__main__':

        sol = Solution()
        method = sol.numIslands3

        cases = [

            (method, ([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]],), 1),
            # (method, (['11000', '11000', '00100', '00011'],), 3),

        ]

        for k, (func, case, expected) in enumerate(cases):
            ans = func(*case)
            if ans == expected:
                print("Case {:d} Passed".format(k + 1))
            else:
                print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k + 1, str(expected), str(ans)))