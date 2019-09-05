"""

373. Find K Pairs with Smallest Sums

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence:
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence:
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

"""

import heapq
import itertools

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        if len(nums1)*len(nums2) <= k:
            return [[i, j] for i, j in itertools.product(nums1, nums2)]

        heap = [(nums1[0]+nums2[0], 0, 0)]
        count = 0
        seq = []
        in_heap = set()
        in_heap.add((0,0))

        while heap:
            sum, i, j = heapq.heappop(heap)
            count += 1
            seq.append([nums1[i], nums2[j]])
            if count == k:
                return seq
            if i + 1 < len(nums1) and (i+1, j) not in in_heap:
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
                in_heap.add((i+1, j))
            if j + 1 < len(nums2) and (i, j+1) not in in_heap:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
                in_heap.add((i, j+1))


if __name__=='__main__':

    sol = Solution()

    cases = [
        # (sol.kSmallestPairs, ([1,7,11], [2,4,6], 3), [[1,2],[1,4],[1,6]]),
        # (sol.kSmallestPairs, ([1,2], [3], 3), [[1,3],[2,3]]),
        (sol.kSmallestPairs, ([-10,-4,0,0,6], [3,5,6,7,8,100], 10), [[-10,3],[-10,5],[-10,6],[-10,7],[-10,8],[-4,3],[-4,5],[-4,6],[0,3],[0,3]]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))