"""


"""

from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        cp, np, ns, cs = Counter(p), len(p), len(s), Counter()
        if ns < np:
            return []

        ans = []
        for i, c in enumerate(s):
            if i < np:
                cs[c] += 1
            else:
                if cs == cp:
                    ans.append(i - np)
                if cs[s[i-np]] == 1:
                    cs.pop(s[i - np])
                else:
                    cs[s[i - np]] -= 1
                cs[c] += 1

        if cp == cs:
            ans.append(ns-np)
        return ans



if __name__=='__main__':

    sol = Solution()
    method = sol.findAnagrams

    cases = [
        (method, ("cbaebabacd", "abc"), [0,6]),
        (method, ("baa", "aa"), [1]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))