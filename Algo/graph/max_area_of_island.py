"""

695. Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

Time: O(n)
Space: O(n)

"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        max_area = 0

        # how to modify recursion depth and return it
        def dfs(x, y, area):
            if grid[x][y] == 1:
                area[0] += 1
                grid[x][y] = 0

                if x + 1 < m and grid[x+1][y] == 1:
                    dfs(x+1, y, area)

                if x - 1 >= 0 and grid[x - 1][y] == 1:
                    dfs(x - 1, y, area)

                if y + 1 < n and grid[x][y+1] == 1:
                    dfs(x, y+1, area)

                if y - 1 >= 0 and grid[x][y-1] == 1:
                    dfs(x, y-1, area)

                return area[0]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j, [0])
                    max_area = max(max_area, area)
        return max_area


if __name__ == '__main__':

        sol = Solution()

        cases = [

            (sol.maxAreaOfIsland, (
                [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                 [0,0,0,0,0,0,0,1,1,1,0,0,0],
                 [0,1,1,0,1,0,0,0,0,0,0,0,0],
                 [0,1,0,0,1,1,0,0,1,0,1,0,0],
                 [0,1,0,0,1,1,0,0,1,1,1,0,0],
                 [0,0,0,0,0,0,0,0,0,0,1,0,0],
                 [0,0,0,0,0,0,0,1,1,1,0,0,0],
                 [0,0,0,0,0,0,0,1,1,0,0,0,0]],
            ), 6),
            (sol.maxAreaOfIsland, ([[0,0,0,0,0,0,0,0]],), 0),
        ]

        for k, (func, case, expected) in enumerate(cases):
            ans = func(*case)
            if ans == expected:
                print("Case {:d} Passed".format(k + 1))
            else:
                print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k + 1, str(expected), str(ans)))