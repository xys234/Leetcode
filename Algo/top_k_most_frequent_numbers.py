"""
347. Top K Frequent Elements


Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

import collections
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = dict(collections.Counter(nums))
        heap = [(f, k) for k, f in freq.items()]
        top_k = heapq.nlargest(k, heap)
        return [k for f, k in top_k]


if __name__=='__main__':

    sol = Solution()

    cases = [
        # (sol.kSmallestPairs, ([1,7,11], [2,4,6], 3), [[1,2],[1,4],[1,6]]),
        # (sol.kSmallestPairs, ([1,2], [3], 3), [[1,3],[2,3]]),
        (sol.topKFrequent, ([1,1,1,2,2,3], 2), [1,2]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))