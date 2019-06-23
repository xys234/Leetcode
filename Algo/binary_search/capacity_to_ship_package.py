"""

1011. Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within D days.

The i-th package on the conveyor belt has a weight of weights[i].
Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages
on the conveyor belt being shipped within D days.



Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation:
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and
splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
Example 2:

Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation:
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:

Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1


Note:

1 <= D <= weights.length <= 50000
1 <= weights[i] <= 500

Review:
2019.06.21

"""

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r, = 1, sum(weights)
        ans = r
        while l < r:
            m = l + (r - l) // 2
            if self.within_ship_period(weights, m, D):
                ans = m
                r = m
            else:
                l = m + 1
        return ans

    @staticmethod
    def within_ship_period(weights, size, days):
        """
        How many days the shipments take for a given size of ship
        :param weights:
        :param size:
        :param days:
        :return:
        """

        n, used = 1, 0
        for weight in weights:
            if weight > size:
                return False
            if used + weight > size:
                n += 1
                used = 0
            used += weight
        return n <= days


if __name__ == '__main__':
    sol = Solution()
    method = sol.shipWithinDays
    # print(sol.within_ship_period([1,2,3,1,1], 2, 4))

    cases = [
        (method, ([1,2,3,4,5,6,7,8,9,10], 5), 15),
        (method, ([3,2,2,4,1,4],3), 6),
        (method, ([1,2,3,1,1],4), 3),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))