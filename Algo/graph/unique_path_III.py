"""

980. Unique Paths III
Hard

"""

from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        unvisited, origin, dest = 0, None, None
        dirs = ((1,0),(0,1),(-1,0),(0,-1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    unvisited += 1
                elif grid[i][j] == 1:
                    origin = (i, j)
                elif grid[i][j] == 2:
                    dest = (i, j)

        def dfs(i, j, unvisited, ans):
            if unvisited == 0:
                for dir in dirs:
                    if 0 <= i+dir[0] < m and 0 <= j+dir[1] < n and grid[i+dir[0]][j+dir[1]] == 2:
                        ans[0] += 1
                return
            elif i == dest[0] and j == dest[1]:
                return

            if i + 1 < m and grid[i+1][j] == 0:
                temp = grid[i+1][j]
                if temp != 2:
                    grid[i+1][j] = 3
                    dfs(i+1, j, unvisited-1, ans)
                    grid[i+1][j] = temp
                else:
                    dfs(i + 1, j, unvisited, ans)

            if i >= 1 and grid[i-1][j] == 0:
                temp = grid[i - 1][j]
                if temp != 2:
                    grid[i - 1][j] = 3
                    dfs(i - 1, j, unvisited - 1, ans)
                    grid[i - 1][j] = temp
                else:
                    dfs(i - 1, j, unvisited, ans)

            if j + 1 < n and grid[i][j+1] == 0:
                temp = grid[i][j+1]
                if temp != 2:
                    grid[i][j+1] = 3
                    dfs(i, j+1, unvisited - 1, ans)
                    grid[i][j+1] = temp
                else:
                    dfs(i, j+1, unvisited, ans)

            if j >= 1 and grid[i][j-1] == 0:
                temp = grid[i][j-1]
                if temp != 2:
                    grid[i][j-1] = 3
                    dfs(i, j-1, unvisited - 1, ans)
                    grid[i][j-1] = temp
                else:
                    dfs(i, j-1, unvisited, ans)

        ans = [0]
        dfs(origin[0], origin[1], unvisited, ans)
        return ans[0]

    def uniquePathsIII_solution(self, grid):
        R, C = len(grid), len(grid[0])

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] in {0, 2}:
                    yield nr, nc

        todo = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != -1: todo += 1
                if val == 1: sr, sc = r, c
                if val == 2: tr, tc = r, c

        self.ans = 0

        def dfs(r, c, todo):
            todo -= 1
            if todo < 0: return
            if r == tr and c == tc:
                if todo == 0:
                    self.ans += 1
                return

            grid[r][c] = -1
            for nr, nc in neighbors(r, c):
                dfs(nr, nc, todo)
            grid[r][c] = 0

        dfs(sr, sc, todo)
        return self.ans

if __name__ == '__main__':

    sol = Solution()
    method = sol.uniquePathsIII

    cases = [
        (method, ([[1,0,0,0],[0,0,0,0],[0,0,2,-1]], ), 2),
        (method, ([[1,0,0,0],[0,0,0,0],[0,0,0,2]], ), 4),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))