"""

174.
Hard

"""

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m - 1 and j == n-1:
                    dungeon[i][j] = max(1, 1-dungeon[i][j])
                elif i == m - 1 and j < n - 1:
                    dungeon[i][j] = max(1, dungeon[i][j+1]-dungeon[i][j])
                elif i < m - 1 and j == n - 1:
                    dungeon[i][j] = max(1, dungeon[i+1][j]-dungeon[i][j])
                else:
                    dungeon[i][j] = min(max(1, dungeon[i][j+1]-dungeon[i][j]), max(1, dungeon[i+1][j]-dungeon[i][j]))

        return dungeon[0][0]


if __name__ == '__main__':
    sol = Solution()
    method = sol.calculateMinimumHP

    cases = [
        (method, ([[-2,-3,3],[-5,-10,1],[10,30,-5]],), 7),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))
