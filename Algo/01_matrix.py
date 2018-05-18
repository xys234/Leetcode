'''
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


'''

# Notes
# BFS to visit vertices multiple times from all zeros


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
                    dist[i][j] == 0
                else:
                    dist[i][j] = MAX_NUM_ELEMENTS
        while queue:
            current = queue.pop(0)
            next = [(current[0] + k[0], current[1] + k[1]) for k in dir]
            for n in next:
                if n[0] >=0 and n[1] >=0 and n[0] < nrows and n[1] < ncols and matrix[n[0]][n[1]] != 0:
                    if dist[n[0]][n[1]] > dist[current[0]][current[1]] + 1:
                        dist[n[0]][n[1]] = dist[current[0]][current[1]] + 1
                        queue.append(n)
        return(dist)
            

if __name__ == "__main__":
    sol = Solution()

    m = [[0,0,0],[0,1,0],[1,1,1]]
    print(m)
    print(sol.updateMatrix(m))


