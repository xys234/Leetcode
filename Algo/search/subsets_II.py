"""

90.

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""


class Solution:
    def subsetsWithDup(self, nums):

        res = set()
        nums.sort()

        def recurse(pre, i):
            if i == len(nums):
                res.add(pre)
                return

            recurse(pre+(nums[i],), i+1)
            recurse(pre, i+1)

        recurse((), 0)
        return [list(e) for e in res]

    def subsetsWithDup_v2(self, nums):

        res = []
        n = len(nums)
        nums.sort()

        def dfs(curr, start_pos, length):
            if len(curr) == length:
                res.append(curr[:])
                return

            for j in range(start_pos, n):
                if j == start_pos or (nums[j] != nums[j-1]):
                    curr.append(nums[j])
                    dfs(curr, j+1, length)
                    curr.pop()

        if n:
            for l in range(n+1):
                dfs([], 0, l)
        return res

if __name__ == '__main__':

    sol = Solution()
    method = sol.subsetsWithDup_v2

    cases = [

        # (method, ([1,2,3], ), [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]),
        # (method, ([1,2,2], ), [[], [1],[2],[1,2],[2,2],[1,2,2]]),
        (method, ([4,4,4,1,4], ), [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]),

             ]

    for k, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if sorted(ans) == sorted(expected):
            print("Case {:d} Passed".format(k + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k+1, str(expected), str(ans)))