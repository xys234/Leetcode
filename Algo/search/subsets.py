"""

78.

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


"""


class Solution:
    def subsets(self, nums):

        res = []
        n = len(nums)

        def dfs(solution, depth):
            if depth == n:
                res.append(solution.copy())
                return

            for s in True, False:
                if s:
                    solution.append(nums[depth])
                dfs(solution, depth+1)
                if solution and s:
                    solution.pop()

        dfs([], 0)
        return res

    def subsets_itertools(self, nums):
        from itertools import chain, combinations
        return [list(c) for c in chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))]

    def subsets_recursive(self, nums):
        results = []

        def powerset(pre, xs):
            if len(xs) == 0:
                results.append(pre)
                return None
            powerset(pre + [xs[0]], xs[1:])
            powerset(pre, xs[1:])

        powerset([], nums)
        return results


if __name__ == '__main__':

    sol = Solution()

    cases = [

        (sol.subsets, ([1,2,3], ), [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]),
        (sol.subsets_itertools, ([1,2,3], ), [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]),
        (sol.subsets_recursive, ([1,2,3], ), [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]),

             ]

    for k, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if sorted(ans) == sorted(expected):
            print("Case {:d} Passed".format(k + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k+1, str(expected), str(ans)))



