"""

282.

Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators (not unary) +, -, or *
between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []

"""


class Solution:
    def addOperators(self, num: str, target: int):
        """

        :param num:
        :param target:
        :rtype list
        """

        pass


if __name__ == '__main__':

    sol = Solution()

    cases = [

        (sol.addOperators, ("aab", ), [["aa","b"], ["a","a","b"]]),
        (sol.addOperators, ("bb", ), [["b","b"], ["bb"]]),

             ]

    for k, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if sorted(ans) == sorted(expected):
            print("Case {:d} Passed".format(k + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k+1, str(expected), str(ans)))
