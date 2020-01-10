"""

1081.
Medium

Example 1:

Input: "cdadabcc"
Output: "adbc"
Example 2:

Input: "abcd"
Output: "abcd"
Example 3:

Input: "ecbacba"
Output: "eacb"
Example 4:

Input: "leetcode"
Output: "letcod"


"""

from collections import Counter


class Solution:
    def smallestSubsequence(self, text: str) -> str:
        count = Counter(text)
        stack = []
        saved = {}

        for c in text:
            count[c] -= 1
            while stack and c < stack[-1] and count[stack[-1]] > 0 and c not in saved:
                saved.pop(stack[-1])
                stack.pop(-1)
            if c not in saved:
                stack.append(c)
                saved[c] = 1

        return ''.join(stack)


if __name__ == '__main__':
    sol = Solution()
    method = sol.smallestSubsequence

    cases = [
        (method, ("cdadabcc",), "adbc"),
        (method, ("abcd",), "abcd"),
        (method, ("ecbacba",), "eacb"),
        (method, ("leetcode",), "letcod"),
        (method, ("abcacb",), "abc"),
        (method, ("cbaacabcaaccaacaba",), "abc"),
        (method, ("cbaacabcaaccaacababa",), "abc"),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))