"""
4.
Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        k = (n1 + n2 + 1) // 2
        l, r = 0, n1
        while l < r:
            m1 = l + (r - l) // 2   # number of elements used
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                l = m1 + 1
            else:
                r = m1

        m1 = l
        m2 = k - m1

        if m1 <= 0:
            c11 = -float('inf')
        else:
            c11 = nums1[m1-1]

        if m2 <= 0:
            c12 = -float('inf')
        else:
            c12 = nums2[m2-1]
        c1 = max(c11, c12)

        if m1 >= n1:
            c21 = float('inf')
        else:
            c21 = nums1[m1]

        if m2 >= n2:
            c22 = float('inf')
        else:
            c22 = nums2[m2]
        c2 = min(c21, c22)

        if (n1+n2) % 2 == 1:
            return c1
        return (c1 + c2) * 0.5


if __name__ == '__main__':
    sol = Solution()
    method = sol.findMedianSortedArrays

    cases = [
        (method, ([1, 3],[2]), 2),
        (method, ([1, 2],[3, 4]), 2.5),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))