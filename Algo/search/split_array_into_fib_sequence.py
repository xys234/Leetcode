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
        n = len(S)
        ans = []

        def dfs(index, prev_seq, current_number):
            if index == n - 1:
                if current_number == sum(prev_seq[-2:]):
                    prev_seq.append(current_number)
                    return True
                else:
                    return False

            current_number = current_number*10 + int(S[index])
            if current_number > 0:
                dfs(index+1, prev_seq, current_number)  # extend the current number if not a zero

            if len(prev_seq) <= 2:
                prev_seq.append(current_number)
                dfs(index+1, prev_seq, 0)
            else:
                if current_number == sum(prev_seq[-2:]):
                    prev_seq.append(current_number)
                    dfs(index + 1, prev_seq, 0)
                else:
                    return

        dfs(0, ans, 0)


if __name__ == '__main__':

    sol = Solution()

    cases = [

        (sol.splitIntoFibonacci, ("123456579", ), [123, 456, 579]),
        # (sol.splitIntoFibonacci, ("1051", 1), ["10+5"]),

             ]

    for k, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(k + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k+1, str(expected), str(ans)))


