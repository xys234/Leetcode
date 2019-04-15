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
    def combinationSum2(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        if not candidates:
            return []

        res = []
        candidates.sort()
        n = len(candidates)

        def dfs(solution, target, last_index):
            """

            :param solution: The current partial solution
            :param target: the current target
            :param used: whether the element has been used
            :return:
            """

            if target == 0:
                res.append(tuple(solution))
                return

            for i in range(last_index, n):
                new_target = target - candidates[i]
                if new_target < 0:
                    break
                else:
                    solution.append(candidates[i])
                    dfs(solution, new_target, i+1)
                    solution.pop()

        dfs([], target, 0)
        return [list(s) for s in set(res)]