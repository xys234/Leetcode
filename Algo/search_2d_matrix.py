"""
73. Search a 2d matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false


Time complexity: O(m+n)
Space complexity: O(m+n)

"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])

        if m == 0 or n == 0:
            return False

        elem_last_col = [r[n - 1] for r in matrix]

        # find the row
        row = min(range(len(elem_last_col)), key=lambda i: abs(elem_last_col[i] - target))
        if matrix[row][n - 1] < target:
            row += 1
        if row >= m:
            return False
        else:
            return target in matrix[row]


if __name__ == "__main__":
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 13

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 51

    sol = Solution()
    print(sol.searchMatrix(matrix, target))