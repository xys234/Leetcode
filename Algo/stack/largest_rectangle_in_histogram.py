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
            while stack and heights[stack[-1]] >= heights[i]:
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1));
        return maxarea

    def max_area_histogram(self, heights):

        # This function calulates maximum
        # rectangular area under given
        # histogram with n bars

        # Create an empty stack. The stack
        # holds indexes of histogram[] list.
        # The bars stored in the stack are
        # always in increasing order of
        # their heights.
        stack = list()

        max_area = 0  # Initialize max area

        # Run through all bars of
        # given histogram
        index = 0
        while index < len(heights):

            # If this bar is higher
            # than the bar on top
            # stack, push it to stack

            if (not stack) or (heights[stack[-1]] <= heights[index]):
                stack.append(index)
                index += 1

            # If this bar is lower than top of stack,
            # then calculate area of rectangle with
            # stack top as the smallest (or minimum
            # height) bar.'i' is 'right index' for
            # the top and element before top in stack
            # is 'left index'
            else:
                # pop the top
                top_of_stack = stack.pop()

                # Calculate the area with
                # histogram[top_of_stack] stack
                # as smallest bar
                area = (heights[top_of_stack] *
                        ((index - stack[-1] - 1)
                         if stack else index))

                # update max area, if needed
                max_area = max(max_area, area)

                # Now pop the remaining bars from
        # stack and calculate area with
        # every popped bar as the smallest bar
        while stack:
            # pop the top
            top_of_stack = stack.pop()

            # Calculate the area with
            # histogram[top_of_stack]
            # stack as smallest bar
            area = (heights[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))

            # update max area, if needed
            max_area = max(max_area, area)

            # Return maximum area under
        # the given histogram
        return max_area


if __name__ == '__main__':

    sol = Solution()
    method = sol.max_area_histogram
    # method = sol.largestRectangleArea

    cases = [
        (method, ([2,1,5,6,2,3],), 10),
        # (method, ([4,6,7],), 12),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))