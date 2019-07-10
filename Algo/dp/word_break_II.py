"""

140.

Hard

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

"""

from typing import List

from collections import Counter


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        mem = {}
        wordDict = Counter(wordDict)

        def helper(xs):
            if xs in mem:
                return mem[xs]

            res = []
            if xs == "":
                return [""]

            for i in range(len(xs)+1):
                if xs[:i] in wordDict:
                    if i == len(xs):    # special case
                        res.append(xs[:i])
                    else:
                        p = helper(xs[i:])
                        for sp in p:
                            res.append(xs[:i]+" "+sp)
            mem[xs] = res
            return res

        return helper(s)

    def wordbreak_recursive(self, s, worddict):
        wordDict = set(worddict)
        partitions = []

        def dfs(curr, xs):
            if not xs:
                partitions.append(curr[:])
                return

            for i in range(len(xs)+1):
                if xs[:i] in worddict:
                    curr.append(xs[:i])
                    dfs(curr, xs[i:])
                    curr.pop()

        dfs([], s)
        return [' '.join(p) for p in partitions]

    def wordbreak_bottom_up(self, s, wordDict):
        worddict = Counter(wordDict)
        n = len(s)
        mem = {}

        for i in range(n+1):
            if s[:i] in worddict:
                mem[i] = [s[:i]]
            for j in range(i-1, -1, -1):
                if s[j:i] in worddict:
                    if j in mem:
                        p = mem[j]
                        for sp in p:
                            res = sp + ' ' + s[j:i]
                            if i in mem:
                                mem[i].append(res)
                            else:
                                mem[i] = [res]
        return mem.get(n, [])


if __name__ == '__main__':

    sol = Solution()

    # print(sol.wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"]))
    # print(sol.wordbreak_bottom_up("catsanddog", ["cats", "dog", "sand", "and", "cat"]))
    # print(sol.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))

    cases = [

        (sol.wordbreak_bottom_up, ("catsanddog", ["cats", "dog", "sand", "and", "cat"]), ["cats and dog", "cat sand dog"]),
        (sol.wordbreak_bottom_up, ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]), ["pine apple pen apple","pineapple pen apple","pine applepen apple"]),
        (sol.wordbreak_bottom_up, ("catsandog", ["cats", "dog", "sand", "and", "cat"]), []),
             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if sorted(ans) == sorted(expected):
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))
