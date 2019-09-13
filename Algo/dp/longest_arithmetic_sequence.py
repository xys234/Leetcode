"""

1027
Medium


"""

from typing import List


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        inc = [1] * n
        step = [0] * n
        max_inc = 1

        for i in range(1, len(A)):
            for j in range(i):
                if A[i] > A[j]:
                    if inc[j] == 1:
                        if inc[j] + 1 > inc[i]:
                            inc[i] = inc[j] + 1
                            step[i] = A[i] - A[j]
                            max_inc = max(max_inc, inc[i])
                    else:
                        if inc[j] + 1 > inc[i] and step[j] + A[j] == A[i]:
                            inc[i] = inc[j] + 1
                            step[i] = step[j]
                            max_inc = max(max_inc, inc[i])

        inc = [1] * n
        step = [0] * n
        max_dec = 1
        for i in range(1, len(A)):
            for j in range(i):
                if A[i] < A[j]:
                    if inc[j] == 1:
                        if inc[j] + 1 > inc[i]:
                            inc[i] = inc[j] + 1
                            step[i] = A[i] - A[j]
                            max_dec = max(max_dec, inc[i])
                    else:
                        if inc[j] + 1 > inc[i] and A[j] + step[j] == A[i]:
                            inc[i] = inc[j] + 1
                            step[i] = step[j]
                            max_dec = max(max_dec, inc[i])

        print((max_inc, max_dec))
        return max(max_inc, max_dec)


if __name__ == "__main__":

    sol = Solution()
    method = sol.longestArithSeqLength

    cases = [
        # (method, ([3,6,9,12],), 4),
        # (method, ([9,4,7,2,10],), 3),
        # (method, ([20,1,15,3,10,5,8],), 4),
        (method, ([58,100,53,24,25,38,44,55,23,17,41,66,10],), 3),

    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i + 1, str(expected), str(ans)))