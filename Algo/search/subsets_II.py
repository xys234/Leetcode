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


if __name__ == '__main__':

    sol = Solution()

    cases = [

        (sol.subsetsWithDup, ([1,2,3], ), [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]),
        (sol.subsetsWithDup, ([1,2,2], ), [[2],[1],[1,2,2],[2,2],[1,2],[]]),
        (sol.subsetsWithDup, ([4,4,4,1,4], ), [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]),

             ]

    for k, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if sorted(ans) == sorted(expected):
            print("Case {:d} Passed".format(k + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k+1, str(expected), str(ans)))