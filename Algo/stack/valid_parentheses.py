"""

20.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

"""


class Solution:
    def isValid(self, s: 'str') -> 'bool':
        """

        :param s:
        :return:

        Time: O(n)
        Space: O(n)

        """
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if stack and stack[-1]+c in ("()","{}","[]"):
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True


if __name__=='__main__':

    sol = Solution()

    cases = [

        (sol.isValid, ("()[]{}",), True),
        (sol.isValid, ("((",), False),
        (sol.isValid, ("}}(",), False),
        (sol.isValid, ("",), True),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))

