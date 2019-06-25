"""



"""


from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        def merge(ia, ib):
            # non-overlapping: a is to b's left
            if ia[1] < ib[0]:
                return [], ib, 'b'

            # non-overlapping: a is to b's right
            elif ia[0] > ib[1]:
                return [], ia, 'a'

            # b is a's subset
            elif ia[0] <= ib[0] and ib[1] <= ia[1]:
                left, right = max(ib[0], ia[0]), min(ib[1], ia[1])
                return [[left, right]], [right, ia[1]], 'a'

            # a is b's subset
            elif ia[0] >= ib[0] and ia[1] <= ib[1]:
                left, right = max(ia[0], ib[0]), min(ia[1], ib[1])
                return [[left, right]], [right, ib[1]], 'b'

            # a is to b's left
            elif ia[0] <= ib[0] <= ia[1] <= ib[1]:
                return [[ib[0], ia[1]]], [ia[1], ib[1]], 'b'

            # a is to b's right
            else:
                return [[ia[0], ib[1]]], [ib[1], ia[1]], 'a'

        a, b, m, res = 0, 0, None, []
        i1, i2 = A[0], B[0]
        while a < len(A) and b < len(B):
            m = merge(i1, i2)
            res.extend(m[0])
            if m[2] == 'a':
                b += 1
                if b < len(B):
                    i1 = m[1]
                    i2 = B[b]
            if m[2] == 'b':
                a += 1
                if a < len(A):
                    i1 = A[a]
                    i2 = m[1]

        return res

    def intervalIntersection_2ptr(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        a, b = 0, 0
        if A and B:
            while a < len(A) and b < len(B):
                lo = max(A[a][0], B[b][0])
                hi = min(A[a][1], B[b][1])
                if lo <= hi:
                    res.append([lo, hi])
                if A[a][1] < B[b][1]:
                    a += 1
                else:
                    b += 1
        return res


if __name__=='__main__':

    def compare_list(ans, expected, type='value'):
        if type == 'equality':
            return ans == expected
        if type == 'item':
            return sorted(ans) == sorted(expected)

    sol = Solution()
    method = sol.intervalIntersection

    cases = [

        (method, ([[3,10]], [[5,10]]), [[5, 10]]),
        (method, ([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]), [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]),
        # (method, ([2,3,5], 8), [[3,5]]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if compare_list(ans, expected, 'item'):
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))
