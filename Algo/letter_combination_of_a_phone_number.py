"""

17.

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.


"""


class Solution:
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        """

        :param digits:
        :return:

        backtracking:
        Time: O(3^n)
        Space: O(3^n) to store answers

        """
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        ans = []
        n = len(digits)
        if n > 0:
            def backtrack(s, curr):
                if len(s) == n:
                    ans.append(''.join(s))
                    return

                letters = digit_to_letters[digits[curr]]
                for letter in letters:
                    s.append(letter)
                    backtrack(s, curr+1)
                    s.pop()

            backtrack([], 0)
        return ans


if __name__=='__main__':

    sol = Solution()

    cases = [

        (sol.letterCombinations, ('23',), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))