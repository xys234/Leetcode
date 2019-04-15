"""

784.

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.

"""

import string


class Solution:
    def letterCasePermutation(self, S: str):

        """



        :param S:
        :return:

            a1b2   i=0, when it's at a, since it's a letter, we have two branches: a, A
         /        \
       a1b2       A1b2 i=1 when it's at 1, we only have 1 branch which is itself
        |          |
       a1b2       A1b2 i=2 when it's at b, we have two branches: b, B
       /  \        / \
      a1b2 a1B2  A1b2 A1B2 i=3  when it's at 2, we only have one branch.
       |    |     |     |
      a1b2 a1B2  A1b2  A1B2 i=4 = S.length(). End recursion, add permutation to ans.

      During this process, we are changing the S char array itself

        """

        n = len(S)
        letters = [letter for letter in S]
        res = []
        used = [False for _ in range(n)]

        def recurse(j=0):
            if j == n:
                res.append("".join(letters))
                return

            if letters[j] in string.ascii_letters:
                letters[j] = letters[j].upper()
                recurse(j+1)
                letters[j] = letters[j].lower()
                recurse(j+1)
            else:
                recurse(j + 1)

        recurse()
        return res


if __name__ == '__main__':

        sol = Solution()

        cases = [

            (sol.letterCasePermutation, ("a1b2",), ["a1b2", "a1B2", "A1b2", "A1B2"]),

        ]

        for k, (func, case, expected) in enumerate(cases):
            ans = func(*case)
            if sorted(ans) == sorted(expected):
                print("Case {:d} Passed".format(k + 1))
            else:
                print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k + 1, str(expected), str(ans)))