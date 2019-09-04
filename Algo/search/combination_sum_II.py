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

    def combinationSum2_v2(self, candidates, target):
        candidates.sort()
        res = []
        n = len(candidates)

        def dfs(curr, curr_sum, d):
            if sum(curr) == target:
                res.append(curr[:])
                return
            if d == n:
                return

            for i in range(d, n):
                if i == d or candidates[i] != candidates[i-1]:
                    if curr_sum + candidates[i] <= target:
                        curr.append(candidates[i])
                        dfs(curr, curr_sum + candidates[i], d + 1)
                        curr.pop()
                    else:
                        break

        dfs([], 0, 0)
        return res

    def combinationSum2_v3(self, candidates, target):
        ans = []
        candidates.sort()

        def dfs(curr, t, start):
            if t == 0:
                ans.append(curr[:])

            for i in range(start, len(candidates)):
                if candidates[i] > t:
                    break
                if i == start or candidates[i-1] != candidates[i]:
                    dfs(curr + [candidates[i]], t - candidates[i], i+1)

        dfs([], target, 0)
        return ans


if __name__=='__main__':

    def compare_list(ans, expected, type='value'):
        if type == 'equality':
            return ans == expected
        if type == 'item':
            return sorted(ans) == sorted(expected)

    sol = Solution()
    method = sol.combinationSum2_v3

    cases = [

        (method, ([2,5,2,1,2], 5), [[1,2,2],[5]]),
        (method, ([2,3,6,7], 7), [[7]]),
        (method, ([2,3,5], 8), [[3,5]]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if compare_list(ans, expected, 'item'):
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))