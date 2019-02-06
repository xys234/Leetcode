"""

Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.
The next row's choice must be in a column that is different from the previous row's column by at most one.



Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation:
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.



Note:

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100


"""

class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        n = len(A)
        dp = [[0]*n for _ in range(n)]
        for j in range(n):
            dp[0][j] = A[0][j]

        for i in range(1, n):
            for j in range(n):
                if 1 <= j <= n-2:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + A[i][j]
                elif j < 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + A[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + A[i][j]


        return min(dp[-1])


if __name__=='__main__':

    sol = Solution()

    cases = [

        (sol.minFallingPathSum, ([[1,2,3],[4,5,6],[7,8,9]],), 12),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))