"""
378.

"""

import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        heap = [(matrix[j][0], j, 0) for j in range(len(matrix))]

        count = 0
        while heap:
            smallest, row, column = heapq.heappop(heap)
            count += 1
            if count == k:
                return smallest
            if column + 1 < len(matrix):
                heapq.heappush(heap, (matrix[row][column+1],row, column+1))


    def find_first_larger_or_equal_element(self, nums, target):
        """
        find the first element larger than or equal to target in a sorted array
        :param nums:
        :param target:
        :return: the index of the element; -1 if there is no such element
        """

        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        while l < r:
            mid = int((l+r)/2)
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid
        if l == r:
            if nums[l] >= target:
                return l
            else:
                return -1
        if l > r:
            return -1

if __name__=='__main__':

    sol = Solution()

    cases = [
        # (sol.find_first_larger_or_equal_element, ([1,2,3,4,5,6,7], 6), 6),
        # (sol.find_first_larger_or_equal_element, ([4,6,7,10], 5), 1),
        # (sol.find_first_larger_or_equal_element, ([4,6,7,10], 3), 0),
        # (sol.find_first_larger_or_equal_element, ([4,6,7,10], 11), -1),
        # (sol.find_first_larger_or_equal_element, ([4], 11), -1),
        # (sol.find_first_larger_or_equal_element, ([1,1,2], 1), 0),
        (sol.kthSmallest, ([[1,5,9],[10,11,13],[12,13,15]], 8), 13),
        (sol.kthSmallest, ([[1,5,9],[4,6,10],[12,13,15]], 8), 13),
        (sol.kthSmallest, ([[1,2],[1,3]], 2), 1),
        (sol.kthSmallest, ([[1,2],[1,3]], 3), 2),
        (sol.kthSmallest, ([[1,3,5],[6,7,12],[11,14,14]], 7), 12),
        (sol.kthSmallest, ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5), 5),
        (sol.kthSmallest, ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20), 21),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))