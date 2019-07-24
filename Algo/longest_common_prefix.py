"""

14.


"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        prefix = ""
        n = len(strs)

        if n == 0:
            return ""

        flag = True
        while flag:
            if i < n and not strs[i]:
                return ""
            if i == len(strs[0]):
                break
            pivot = strs[0][i]
            for j in range(1, n):
                if i >= len(strs[j]):
                    flag = False
                    break
                elif strs[j][i] != pivot:
                    flag = False
                    break
            if flag:
                prefix += pivot
                i += 1
        return prefix


if __name__ == '__main__':

    sol = Solution()

    cases = [

        (sol.longestCommonPrefix, (["flower","flow","flight"], ), "fl"),
        (sol.longestCommonPrefix, (["dog","racecar","car"], ), ""),
        (sol.longestCommonPrefix, (["a"], ), "a"),
        (sol.longestCommonPrefix, (["c", "c"], ), "c"),
        # (sol.subsets_itertools, ([1,2,3], ), [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]),
        # (sol.subsets_recursive, ([1,2,3], ), [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]),

             ]

    for k, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(k + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k+1, str(expected), str(ans)))