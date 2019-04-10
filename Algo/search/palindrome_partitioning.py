"""

131. Palindrome Partitioning

Medium


Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

"""

from collections import defaultdict


class Solution:
    def partition(self, s):

        n = len(s)
        if n == 1:
            return [[s]]

        res = []

        def is_palindrome(seq):
            for i in range(len(seq)):
                if seq[i] != seq[len(seq) - i - 1]:
                    return False
            return True

        def dfs(start_index, curr):
            if start_index == n:
                res.append(curr[:])
                return

            for i in range(start_index+1, n+1):
                if is_palindrome(s[start_index:i]):
                    curr.append(s[start_index:i])
                    dfs(i, curr)
                    curr.pop(-1)

        dfs(0, [])
        return res

    def partition_faster(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = [[]]
        for c in s:
            for i in range(len(res)):
                l = res[i]
                if len(l)>0 and l[-1]==c:
                    res.append(l[:-1]+[c*2])
                if len(l)>1 and l[-2]==c:
                    res.append(l[:-2]+[c+l[-1]+c])
                res[i].append(c)
        return res


if __name__ == '__main__':

    sol = Solution()

    cases = [

        (sol.partition_faster, ("aab", ), [["aa","b"], ["a","a","b"]]),
        (sol.partition, ("bb", ), [["b","b"], ["bb"]]),

             ]

    for k, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if sorted(ans) == sorted(expected):
            print("Case {:d} Passed".format(k + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k+1, str(expected), str(ans)))