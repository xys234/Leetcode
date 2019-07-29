"""

315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.


"""

from typing import List


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0 for _ in range(n+1)]

    def query(self, idx):
        s = 0
        idx += 1

        # Traverse ancestors of BITree[index]
        while idx > 0:
            # Add current element of BITree to sum
            s += self.bit[idx]

            # Move index to parent node in getSum View
            idx -= idx & (-idx)
        return s

    def update(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & (-idx)


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sorted_nums = sorted(nums)
        ranks, rank = {}, 0
        for i, num in enumerate(sorted_nums):
            if not ranks or num == sorted_nums[i-1]:
                ranks[num] = rank
            else:
                rank += 1
                ranks[num] = rank

        # ranks = {v:i for i, v in enumerate(sorted(nums))}

        tree = FenwickTree(n)
        count = []

        for num in reversed(nums):
            rank = ranks[num]
            tree.update(rank, 1)
            count.append(tree.query(rank-1))

        return list(reversed(count))

    def countSmaller_bisect(self, nums: List[int]) -> List[int]:
        import bisect
        fir, sec, res = [], [], []
        for i in nums[::-1]:
            res += [bisect.bisect_left(fir,i) + bisect.bisect_left(sec,i)]
            bisect.insort_left(sec,i)
            if len(fir) < 4*len(sec):
                fir = sorted(fir+sec)
                sec = []
        return res[::-1]


if __name__ == '__main__':

    sol = Solution()
    method = sol.countSmaller

    cases = [

        # (method, ([5, 2, 6, 1],), [2, 1, 1, 0]),
        # (method, ([-1, -1],), [0, 0]),
        (method, ([-1, -2],), [1, 0]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))