"""
40.


Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]


"""

class Solution:
    def combinationSum2(self, candidates, target):

        res = set()
        candidates.sort()
        n = len(candidates)

        def recurse(solution, start_index, t):
            if t == 0:
                res.add(solution)
                return

            if start_index >= n:
                return

            for i in range(start_index, n):
                new_target = t - candidates[i]
                if new_target < 0:
                    break
                recurse(solution+(candidates[i],), i+1, new_target)

        recurse(tuple(), 0, target)
        return [list(s) for s in res]


if __name__=='__main__':

    def compare_list(ans, expected, type='value'):
        if type == 'equality':
            return ans == expected
        if type == 'item':
            return sorted(ans) == sorted(expected)

    sol = Solution()

    cases = [

        (sol.combinationSum2, ([2,3,6,7], 7), [[7]]),
        (sol.combinationSum2, ([2,3,5], 8), [[3,5]]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if compare_list(ans, expected, 'item'):
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))