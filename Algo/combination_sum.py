"""

39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

"""


class Solution:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':

        ans = []
        n = len(candidates)
        candidates.sort()
        def backtrack(combo, curr_sum, curr_index):
            if curr_sum == target:
                ans.append(combo[:])
                return True
            elif curr_sum > target:
                return False
            else:
                for i in range(curr_index, n):
                    if candidates[i] + curr_sum > target:
                        return
                    combo.append(candidates[i])
                    curr_sum += candidates[i]
                    backtrack(combo, curr_sum, i)
                    combo.pop()
                    curr_sum -= candidates[i]

        backtrack([], 0, 0)
        return ans


if __name__=='__main__':

    sol = Solution()

    cases = [

        (sol.combinationSum, ([2,3,6,7], 7), [[7],[2,2,3]]),
        (sol.combinationSum, ([2,3,5], 8), [[2,2,2,2],[2,3,3],[3,5]]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))