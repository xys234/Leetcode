"""

139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false


"""

class Solution(object):
    def wordBreak_Slow(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        wordDict = {w:1 for w in wordDict}
        n = len(s)
        dp1 = [wordDict.get(s[:i],0) for i in range(0, n+1)]
        dp2 = [0]*(n+1)
        k = 2
        found=False

        while k <= n and not found:
            for i in range(k, n+1):
                for j in range(k-1, i):
                    dp2[i] = max(dp2[i], dp1[j]*wordDict.get(s[j:i], 0))
            if dp2[n]:
                found = True
            dp1, dp2 = dp2, [0]*(n+1)
            k += 1
        return found

    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        mems = dict()
        mems[""] = True

        def word_break(s, mems):

            if s in mems:
                return mems[s]

            if s in wordDict:
                mems[s] = True
                return True

            for i, _ in enumerate(s):
                left = s[:i]
                right = s[i:]
                if word_break(left, mems) and right in wordDict:
                    mems[s] = True
                    return True
            mems[s] = False
            return False
        return word_break(s, mems)



if __name__=='__main__':

    sol = Solution()

    cases = [

        (sol.wordBreak, ("leetcode", ["leet", "code"]), True),
        (sol.wordBreak, ("applepenapple", ["apple", "pen"]), True),
        (sol.wordBreak, ("catsandog", ["cats", "dog", "sand", "and", "cat"]), False),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))