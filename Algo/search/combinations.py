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


if __name__ == '__main__':

    sol = Solution()

    cases = [

        (sol.combine, (4, 2), [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]),
        (sol.combine_itertools, (4, 2), [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]),

             ]

    for k, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if sorted(ans) == sorted(expected):
            print("Case {:d} Passed".format(k + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k+1, str(expected), str(ans)))

