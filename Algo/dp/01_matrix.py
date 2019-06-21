"""

542 Medium

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.

# Notes
# BFS to visit vertices multiple times from all zeros

Review
2019.02.06 For distance, consider known algorithm such as BFS, DFS and DP
2019.06.19

"""


class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]

        matrix is stored row-wise

        """
        dir = [(-1,0),(1,0),(0,-1),(0,1)]   
        MAX_NUM_ELEMENTS = 10000

        nrows = len(matrix)
        ncols = len(matrix[0])

        dist = [[0 for c in range(ncols)] for r in range(nrows)]

        queue = []

        # Push all the zeros to the queue to find all paths from all 0s
        for i in range(0, nrows):
            for j in range(0, ncols):
                if matrix[i][j] == 0:
                    queue.append((i,j))
                else:
                    dist[i][j] = MAX_NUM_ELEMENTS
        while queue:
            current = queue.pop(0)
            next = [(current[0] + k[0], current[1] + k[1]) for k in dir]
            for n in next:
                if 0 <= n[0] < nrows and 0 <= n[1] < ncols and matrix[n[0]][n[1]] != 0:
                    if dist[n[0]][n[1]] > dist[current[0]][current[1]] + 1:
                        dist[n[0]][n[1]] = dist[current[0]][current[1]] + 1
                        queue.append(n)
        return dist

    def updateMatrix2(self, matrix):
        """
        BFS
        :param matrix:
        :return:
        """
        m, n = len(matrix), len(matrix[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        q = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j))
                else:
                    res[i][j] = float('inf')

        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while q:
            r, c = q.pop(0)
            for dir in dirs:
                if 0 <= r+dir[0] < m and 0 <= c+dir[1] < n and matrix[r+dir[0]][c+dir[1]] == 1:

                    if res[r+dir[0]][c+dir[1]] > res[r][c] + 1:
                        res[r+dir[0]][c+dir[1]] = res[r][c] + 1
                        q.append((r + dir[0], c + dir[1]))
        return res

    def updateMatrix3(self, matrix):
        """
        DP
        :param matrix:
        :return:
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i < m-1:
                        dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                    if j < n-1:
                        dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        return dp


if __name__ == '__main__':
    sol = Solution()
    method = sol.updateMatrix3

    cases = [
        (method, ([[0,0,0], [0,1,0], [0,0,0]],), [[0,0,0], [0,1,0], [0,0,0]]),
        (method, ([[0,0,0], [0,1,0], [1,1,1]],), [[0,0,0], [0,1,0], [1,2,1]]),
        (method, ([[0,0,0], [1,1,0], [1,1,1]],), [[0,0,0], [1,1,0], [2,2,1]]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))


