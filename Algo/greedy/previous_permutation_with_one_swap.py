"""

1053.

Given an array A of positive integers (not necessarily distinct),
return the lexicographically largest permutation that is smaller than A, that can be made with one swap
(A swap exchanges the positions of two numbers A[i] and A[j]).  If it cannot be done, then return the same array.



Example 1:

Input: [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.
Example 2:

Input: [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.
Example 3:

Input: [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.
Example 4:

Input: [3,1,1,3]
Output: [1,3,1,3]
Explanation: Swapping 1 and 3.

"""

from typing import List


class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        ind = None
        for i in range(len(A) - 1, -1, -1):
            if i - 1 >= 0 and A[i - 1] > A[i]:
                ind = i - 1
                break

        # If no such index, return original array A
        if ind == None:
            return A

        mx = float('-inf')

        for i in range(ind + 1, len(A)):
            if A[i] > mx and A[i] < A[ind]:
                mx = A[i]
                mxind = i

            # Simple Swap
        temp = A[ind]
        A[ind] = A[mxind]
        A[mxind] = temp

        return A


if __name__ == '__main__':
    sol = Solution()
    method = sol.prevPermOpt1

    cases = [
        (method, ([1,9,4,6,7],), [1,7,4,6,9]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))
