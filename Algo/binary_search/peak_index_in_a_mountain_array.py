"""
852. Peak Index in a Mountain Array

Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that
A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.


"""


class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        l, r = 0, len(A)-1
        while l < r:
            mid = int((l+r)/2)
            if len(A) - 1 > mid > 0 and A[mid+1] < A[mid] > A[mid-1]:   # solution condition
                return mid
            elif A[mid] < A[mid+1]:                             # otherwise, eliminate half
                l = mid + 1
            elif A[mid] < A[mid-1]:
                r = mid - 1
        return l

    def peakIndexInMountainArray2(self, A):
        pass

if __name__ == '__main__':

    sol = Solution()

    cases = [

        (sol.peakIndexInMountainArray, ([0,2,1,0],), 1),
        (sol.peakIndexInMountainArray, ([0,3,2,1,0],), 1),
        (sol.peakIndexInMountainArray, ([0,1,0],), 1),
        (sol.peakIndexInMountainArray, ([0,1,2,3,4,2],), 4),
             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))