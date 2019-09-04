"""

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]


"""


class Solution:
    def combine(self, n: int, k: int):
        res = []

        def dfs(solution, start):
            if len(solution) == k:
                res.append(solution.copy())
                return

            for i in range(start, n+1):
                solution.append(i)
                dfs(solution, i+1)
                solution.pop()

        dfs([], 1)
        return res

    def combine_itertools(self, n, k):
        from itertools import combinations
        return [list(c) for c in combinations(list(range(1, n+1)), k)]

    def combine2(self, n, k):
        ans = []

        def dfs(start, curr_k, curr):
            if curr_k == k:
                ans.append(curr[:])
                return

            for i in range(start, n+1):
                dfs(i+1, curr_k+1, curr+[i])

        dfs(1, 0, [])
        return ans


if __name__ == '__main__':

    sol = Solution()
    method = sol.combine2

    cases = [

        (method, (4, 2), [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]),

             ]

    for k, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if sorted(ans) == sorted(expected):
            print("Case {:d} Passed".format(k + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k+1, str(expected), str(ans)))

