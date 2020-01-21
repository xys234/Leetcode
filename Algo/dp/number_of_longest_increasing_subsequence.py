"""

673.
Medium


"""

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        lengths, counts = [1]*n, [1]*n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        max_length = max(lengths)
        ans = 0
        for length, count in zip(lengths, counts):
            if length == max_length:
                ans += count
        return ans

    def findNumberOfLIS2(self, nums):
        n = len(nums)
        length = [1 for _ in nums]
        count = [1 for _ in nums]

        max_len, max_count = 1, 1
        for i in range(1, n):
            curr_len = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[j] + 1 > curr_len:
                        curr_len = length[j] + 1
                        count[i] = count[j]
                        length[i] = curr_len
                    elif length[j] + 1 == curr_len:
                        count[i] += count[j]
            max_len = max(max_len, curr_len)

        total_count = 0
        for l, c in zip(length, count):
            if l == max_len:
                total_count += c
        return total_count


if __name__ == "__main__":

    sol = Solution()
    method = sol.findNumberOfLIS2

    cases = [
        (method, ([1,3,5,4,7],), 2),
        (method, ([1,3,2],), 2),
        (method, ([1,2,3,1,2,3,1,2,3],), 10),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))