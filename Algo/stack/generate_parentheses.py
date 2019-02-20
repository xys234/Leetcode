"""

22.

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


2019/02/20: First attempt after solution

"""

class Solution(object):
    def generateParenthesis_solution(self, N):
        ans = []

        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * N:
                ans.append(s)
                return
            if left < N:
                backtrack(s+'(', left+1, right)
            if right < left:
                backtrack(s+')', left, right+1)

        backtrack()
        return ans

    def generateParenthesis(self, N):
        """

        :param N:
        :return:

        Recursive backtracking
        Key insights: Append left parenthesis first,
        if # right < # left place right parenthesis

        """
        ans = []

        def generate_parenthesis_backtrack(s, left, right):
            if len(s) == 2*N:
                ans.append(s)
                return
            if left < N:
                generate_parenthesis_backtrack(s+'(', left+1, right)
            if right < left:
                generate_parenthesis_backtrack(s+')', left, right+1)
        generate_parenthesis_backtrack('', 0, 0)
        return ans


if __name__=='__main__':

    sol = Solution()

    cases = [

        (sol.generateParenthesis, (3,), True),


             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))