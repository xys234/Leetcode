"""

842.

Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes,
except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.

"""


class Solution:
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        self.dfs(S, [], res)
        return res

    def dfs(self, num_str, path, res):
        if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
            return False
        if not num_str and len(path) >= 3:
            res.extend(path)
            return True
        for i in range(len(num_str)):
            curr = num_str[:i + 1]
            if (curr[0] == '0' and len(curr) != 1) or int(curr) >= 2 ** 31:
                continue
            if self.dfs(num_str[i + 1:], path + [int(curr)], res):
                return True

    def split_fib(self, s):

        MAX = 2 ** 31
        n = len(s)
        res = []

        def recurse(current_seq, start_index):
            if start_index >= n and len(current_seq) >= 3 and current_seq[-1] == current_seq[-2] + current_seq[-3]:
                res.extend(current_seq)
                return True

            if len(current_seq) >= 3 and current_seq[-1] != current_seq[-2] + current_seq[-3]:
                return False

            for i in range(start_index, n):
                num_str = s[start_index:i+1]
                num = int(num_str)
                if len(num_str) > 1 and num_str[0] == '0' or num >= MAX:
                    continue
                if recurse(current_seq + [num], i + 1):
                    return True

        recurse([], 0)
        return res


if __name__ == '__main__':

    sol = Solution()

    cases = [

        (sol.split_fib, ("123456579", ), [123, 456, 579]),
        (sol.split_fib, ("11235813", ), [1,1,2,3,5,8,13]),
        (sol.splitIntoFibonacci, ("112358130", ), []),

             ]

    for k, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(k + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k+1, str(expected), str(ans)))


