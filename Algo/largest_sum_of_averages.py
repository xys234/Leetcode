"""

813. Largest Sum of Averages

We partition a row of numbers A into at most K adjacent (non-empty) groups,
then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input:
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation:
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.


Note:

1 <= A.length <= 100.
1 <= A[i] <= 10000.
1 <= K <= A.length.
Answers within 10^-6 of the correct answer will be accepted as correct.

"""

class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """

        n = len(A)
        dp = [[0]*(n+1) for _ in range(K+1)]

        # precompute the sums
        _sums = [0]*(n+1)
        for i in range(1,n+1):
            _sums[i] = _sums[i-1] + A[i-1]
            dp[1][i] = _sums[i]*1.0 / i

        for k in range(2, K+1):
            for i in range(k, n+1):
                for j in range(k-1, i):
                    dp[k][i] = max(dp[k][i], dp[k-1][j] + (_sums[i]-_sums[j])*1.0/(i-j))
        return dp[K][n]


if __name__=='__main__':

    sol = Solution()

    cases = [

        # (sol.largestSumOfAverages, ([9,1,2,3,9], 3), 20),
        (sol.largestSumOfAverages, ([1,2,3,4,5,6,7],4), 20.5),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))