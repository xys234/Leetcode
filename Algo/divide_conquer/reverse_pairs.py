"""

493. Reverse Pairs

Hard

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.

History:
2019.07.15     Read Answer

"""

from typing import List
from bisect import bisect, bisect_right


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        merged, pairs = self.helper(nums)
        return pairs

    def helper(self, nums):
        n = len(nums)
        if n == 1:
            return nums, 0

        mid = n // 2
        merged_left, pairs_left = self.helper(nums[:mid])
        merged_right, pairs_right = self.helper(nums[mid:])
        merged, pairs_cross = self.merge(merged_left, merged_right)
        return merged, pairs_left + pairs_cross + pairs_right

    @staticmethod
    def merge(arr1, arr2):
        """
        Merge two sorted arrays and return the number of reverse pairs
        :param arr1:
        :param arr2:
        :return:
        """

        if not arr1:
            return arr2

        if not arr2:
            return arr1

        merged, pairs = [], 0
        p, q = 0, 0
        n, m = len(arr1), len(arr2)

        # Count the pair
        while p < n and q < m:
            if arr1[p] > 2*arr2[q]:
                pairs += n - p
                q += 1
            else:
                p += 1

        # Merge
        p, q = 0, 0
        while p < n and q < m:
            if arr1[p] <= arr2[q]:
                merged.append(arr1[p])
                p += 1
            else:
                merged.append(arr2[q])
                q += 1

        if p < n:
            merged.extend(arr1[p:])

        if q < m:
            merged.extend(arr2[q:])

        return merged, pairs

    def reversePairs_bisect(self, nums: List[int]) -> int:
        out = 0
        seen = []
        for num in nums:
            out += (len(seen) - bisect(seen, 2*num))
            idx = bisect_right(seen, num)
            seen[idx:idx] = [num]
        return out


if __name__ == "__main__":
    sol = Solution()
    method = sol.reversePairs

    sol.merge([2, 4], [1,3,5])

    cases = [
        (method, ([1,3,2,3,1], ), 2),
        (method, ([2,4,3,5,1], ), 3),
        (method, ([[-5,-5]], ), 1),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))