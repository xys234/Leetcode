"""

216.

Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]


"""


class Solution:
    def combinationSum3(self, k: int, n: int):
        res = []

        def recurse(solution, num, target):
            if len(solution) == k and target == 0:
                res.append(solution[:])

            for j in range(num, 10):
                new_target = target - j
                if new_target < 0:
                    break

                recurse(solution + [j], j+1, new_target)

        recurse([], 1, n)
        return res

    def combinationSum3_v2(self, k, n):
        ans = []

        def dfs(start, curr_k, curr_target, curr):
            if curr_k == k and curr_target == 0:
                ans.append(curr[:])

            for i in range(start, 10):
                if i > curr_target:
                    break

                dfs(i+1, curr_k-1, curr_target-i, curr+[i])

        dfs(1, 0, n, [])
        return ans


if __name__ == '__main__':

        sol = Solution()

        cases = [

            (sol.combinationSum3, (3, 7), [[1, 2, 4]]),
            (sol.combinationSum3, (3, 9), [[1, 2, 6], [1, 3, 5], [2, 3, 4]]),

        ]

        for k, (func, case, expected) in enumerate(cases):
            ans = func(*case)
            if sorted(ans) == sorted(expected):
                print("Case {:d} Passed".format(k + 1))
            else:
                print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k + 1, str(expected), str(ans)))