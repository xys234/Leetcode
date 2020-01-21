"""

220. medium

Given an array of integers, find out whether there are two distinct indices i and j in the array such that
the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j
is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

2019.02.07 Reviewed; Group numbers into ranges with centers at t, 2t, 3t...,
"""

import bisect

class Solution:
    def containsNearbyAlmostDuplicate_brute_force(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        for i, _ in enumerate(nums):
            for d in range(-k, k+1):
                if d != 0 and i+d >= 0 and i+d < len(nums):
                    if abs(nums[i] - nums[i+d]) <=t:
                        return True
        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        window = []
        for i, num in enumerate(nums):
            ind = bisect.bisect_left(window, num)
            window.insert(ind, num)
            if len(window) > k+1:
                pop_ind = bisect.bisect_left(window, nums[i-k-1])
                window.pop(pop_ind)
                if ind > 0:
                    ind -= 1

            if len(window) > 1:
                if ind + 1 >= len(window):
                    if abs(window[ind] - window[ind-1]) <= t:
                        return True
                elif ind - 1 < 0:
                    if abs(window[ind] - window[ind+1]) <= t:
                        return True
                else:
                    if abs(window[ind] - window[ind+1]) <= t or abs(window[ind] - window[ind-1]) <= t:
                        return True
        return False

    def containsNearbyAlmostDuplicate_solution(self, nums, k: int, t: int) -> bool:

        if t == 0 and len(nums) == len(set(nums)):
            return False

        for i, val in enumerate(nums):
            for j in range(i + 1, i + k + 1):
                if j >= len(nums):
                    break
                if abs(nums[j] - val) <= t:
                    return True

        return False


if __name__ == '__main__':
    # cases = [
        # ([1, 2, 3, 1], 3, 0),
        # ([1,0,1,1], 1, 2),
        # (),
        # ([3,6,0,4], 2, 2),

    # ]

    sol = Solution()
    method = sol.containsNearbyAlmostDuplicate

    cases = [

        # (method, ([1, 2, 3, 1], 3, 0,), True),
        # (method, ([1,5,9,1,5,9], 2, 3), False),
        (method, ([1, 2, 3, 1], 1, 0,), False),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))