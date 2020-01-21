"""

845. Longest Mountain in Array

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000


Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?

"""

from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        if n <= 2:
            return 0

        curr, prev, inc_len, dec_len, max_len = 1, 0, 0, 0, 0
        while curr < n:
            if A[curr] > A[prev]:
                if dec_len == 0:
                    if inc_len == 0:
                        inc_len += 2
                    else:
                        inc_len += 1
                else:
                    inc_len = 2
                    dec_len = 0
            elif A[curr] < A[prev] and inc_len > 0:
                if dec_len == 0:
                    dec_len = 1
                else:
                    dec_len += 1
            else:
                inc_len, dec_len = 0, 0

            if inc_len > 0 and dec_len > 0:
                max_len = max(max_len, inc_len+dec_len)
            prev, curr = curr, curr + 1
        return max_len

    def longestMountain2(self, A):
        n = len(A)

        if n <= 2:
            return 0

        ans = 0
        start = 0
        while start < n:
            end = start
            if end < n - 1 and A[end] < A[end+1]:
                while end < n - 1 and A[end] < A[end+1]:
                    end += 1

                # if a peak is found, try to extend it
                if end < n - 1 and A[end] > A[end+1]:
                    while end < n - 1 and A[end] > A[end+1]:
                        end += 1
                    ans = max(ans, end-start+1)
            start = max(end, start+1)
        return ans


if __name__=="__main__":
    sol = Solution()
    method = sol.longestMountain2

    cases = [
        (method, ([2,1,4,7,3,2,5],), 5),
        (method, ([2,2,2],), 0),
        (method, ([1,4,2,3,4,5,3,1],), 6),
        (method, ([2,3,3,2,0,2],), 0),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))
