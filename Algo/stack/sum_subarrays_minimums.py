"""

907

Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.



Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.


Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000

"""


class Solution(object):
    def sumSubarrayMins(self, A):
        """

        :param A:
        :return:

        Iterate from left to right; The iterating element is the right most element.
        Note down the current minimum pattern and the sum

        Time: O(n)
        Space: O(n)

        """
        MOD = 10**9 + 7
        stack = []
        dot = ans = 0
        for _, a in enumerate(A):
            count = 1
            while stack and stack[-1][0] >= a:
                x, c = stack.pop()
                count += c
                dot -= x*c
            stack.append((a, count))
            dot += a*count
            ans += dot
        return ans % MOD

if __name__=='__main__':

    sol = Solution()

    cases = [

        # (sol.sumSubarrayMins, ([1,7],), 9),
        # (sol.sumSubarrayMins, ([6,7,5],), 34),
        # (sol.sumSubarrayMins, ([48, 87, 27],), 264),
        # (sol.sumSubarrayMins, ([3,1,2,4],), 17),
        # (sol.sumSubarrayMins, ([4,3,1,4],), 17),
        (sol.sumSubarrayMins, ([1,2,3,4],), 17),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))