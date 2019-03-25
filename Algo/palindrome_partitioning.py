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


class Solution:
    def partition(self, s: str):

        n = len(s)
        if n == 1:
            return [s]

        res = []

        def is_palindrome(seq: str):
            return seq == "".join(reversed(seq))

        def dfs(start_index, curr):
            if start_index == n - 1:
                curr.append(s[start_index])
                res.append(curr)
                return True

            for i in range(start_index+1, n):
                if is_palindrome(s[start_index:i]):
                    curr.append(s[start_index:i])
                    curr2 = curr[:]
                    dfs(i, curr)
                    curr = curr2
                else:
                    return False

        dfs(0, [])
        return res


if __name__ == '__main__':

    sol = Solution()

    cases = [

        (sol.partition, ("aab", ), [["aa","b"], ["a","a","b"]]),

             ]

    for k, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(k + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k+1, str(expected), str(ans)))