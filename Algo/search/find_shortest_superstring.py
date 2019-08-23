"""

943.

Given an array A of strings, find any smallest string that contains each string in A as a substring.

We may assume that no string in A is substring of another string in A.


Example 1:

Input: ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
Example 2:

Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"


Note:

1 <= A.length <= 12
1 <= A[i].length <= 20

"""


class Solution:
    def shortestSuperstring(self, A) -> str:

        n = len(A)
        g = {}
        for i in range(n):
            for j in range(n):
                if i != j:
                    g[(i, j)] = self.cost(A[i], A[j])

        # Hamiltonian path in a weighted graph


    # length of the superstring if w2 is appended to the end of w1
    @staticmethod
    def cost(w1, w2):
        l = min(len(w1), len(w2))
        while l >= 0:
            if w2[:l] == w1[-l:]:
                break
            else:
                l -= 1
        return len(w1)+len(w2)-l






if __name__ == '__main__':

    sol = Solution()
    print(sol.cost("catg", "atgcatc"))


    # cases = [
    #
    #     # (sol.addOperators, ("115", 115), ["115"]),
    #     (sol.shortestSuperstring, ("1051", 1), ["10+5"]),
    #
    #          ]
    #
    # for k, (func, case, expected) in enumerate(cases):
    #     ans = func(*case)
    #     if sorted(ans) == sorted(expected):
    #         print("Case {:d} Passed".format(k + 1))
    #     else:
    #         print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k+1, str(expected), str(ans)))
