"""


"""

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        x, y, smallest = 0, 0, 1
        seq = [matrix[x][y]]
        while smallest < k:
            candidates = []
            if x - 1 >= 0:
                arr_above = matrix[x-1][y+1:]
                larger_elem = self.find_first_larger_or_equal_element(arr_above, matrix[x][y])
                if larger_elem > -1:
                    candidates += [(x - 1, y+1+larger_elem)]
            if x + 1 < len(matrix):
                arr_below = matrix[x+1][:y+1]
                larger_elem = self.find_first_larger_or_equal_element(arr_below, matrix[x][y])
                if larger_elem > -1:
                    candidates += [(x + 1, larger_elem)]
            # add column binary search
            if y + 1 < len(matrix[0]):
                candidates += [(x, y+1)]
            if candidates:
                smallest_x, smallest_y = candidates[0]
            else:
                # error
                return -1
            for j, c in enumerate(candidates):
                if j > 0 and matrix[x][y] <= matrix[c[0]][c[1]] < matrix[smallest_x][smallest_y]:
                    smallest_x, smallest_y = c
            smallest += 1
            x, y = smallest_x, smallest_y
            seq.append(matrix[x][y])
        return matrix[x][y]

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
        # (sol.kthSmallest, ([[1,5,9],[10,11,13],[12,13,15]], 8), 13),
        # (sol.kthSmallest, ([[1,5,9],[4,6,10],[12,13,15]], 8), 13),
        # (sol.kthSmallest, ([[1,2],[1,3]], 2), 1),
        # (sol.kthSmallest, ([[1,2],[1,3]], 3), 2),
        # (sol.kthSmallest, ([[1,3,5],[6,7,12],[11,14,14]], 7), 12),
        (sol.kthSmallest, ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5), 5),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))