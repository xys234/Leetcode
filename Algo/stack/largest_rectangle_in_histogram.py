"""

88.

Hard

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.

[2,1,5,6,2,3]. the max area is 10

History:
2019.07.12

"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        stack = [-1]
        maxarea = 0
        for i in range(len(heights)):
            while stack and stack[-1] >= 0 and heights[stack[-1]] >= heights[i]:
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1));
        return maxarea


if __name__ == '__main__':

    sol = Solution()
    method = sol.largestRectangleArea

    cases = [
        # (method, ([2,1,5,6,2,3],), 10),
        # (method, ([4,6,7],), 12),
        # (method, ([3,2,2],), 6),
        (method, ([1,2,4],), 4),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))