"""

42.
Hard

"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        dp_right = [-1 for _ in height]
        left_max, dp_right[-1] = height[0], height[-1]

        for j in range(len(height)-2, -1, -1):
            dp_right[j] = max(dp_right[j+1], height[j])

        water = 0
        for i, (h, r) in enumerate(zip(height, dp_right)):
            if h > left_max:
                left_max = h
            water += max(0, min(left_max, r)-h)
        return water


if __name__ == '__main__':
    sol = Solution()
    method = sol.trap

    cases = [
        (method, ([0,1,0,2,1,0,1,3,2,1,2,1],), 6),
        (method, ([2,0,2],), 2),
        (method, ([5,4,1,2],), 1),
        (method, ([5,2,1,2,1,5],), 14),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))

