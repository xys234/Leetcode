"""

854.
Hard

"""

import collections


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        A, B = self.trim(A, B)
        if A == B:
            return 0
        memo = {}
        self.target_swap(A, B, memo)
        return memo[(A, B)]

    @staticmethod
    def trim(A, B):
        newA, newB = [], []

        for a, b in zip(A, B):
            if a != b:
                newA.append(a)
                newB.append(b)

        return ''.join(newA), ''.join(newB)

    def target_swap(self, s, target, memo):
        """
        The minimum number of swaps to transform s to target
        :param s:
        :param target:
        :param memo:
        :return:
        """

        if s == target:
            return 0

        if (s, target) in memo:
            return memo[(s, target)]

        ans = float('inf')
        s, target = self.trim(s, target)

        for i, c in enumerate(s):
            if c == target[0]:
                new_s = self.swap(s, 0, i)[1:]
                new_target = target[1:]
                res = 1 + self.target_swap(new_s, new_target, memo)
                ans = min(ans, res)
        memo[(s, target)] = ans
        return ans

    @staticmethod
    def swap(s, i, j):
        l = [c for c in s]
        l[i], l[j] = l[j], l[i]
        return ''.join(l)

    def kSimilarity_solution(self, A, B):
        if A == B: return 0
        dq, seen, step, n = collections.deque([A]), {A}, 0, len(A)
        while dq:
            sz = len(dq)
            for _ in range(sz):
                cur, i = dq.popleft(), 0
                while i < n and cur[i] == B[i]:
                    i += 1
                for j in range(i + 1, n):
                    if B[j] != cur[i] or cur[j] == B[j]: continue
                    nxt = cur[:i] + cur[j] + cur[i + 1: j] + cur[i] + cur[j + 1:]
                    if nxt not in seen:
                        seen.add(nxt)
                        if nxt == B: return step + 1
                        dq.append(nxt)
            step += 1


if __name__ == "__main__":

    sol = Solution()
    method = sol.kSimilarity

    cases = [

        (method, ("abc","bca"), 2),
        (method, ("abac","baca"), 2),
        (method, ("aabc","abca"), 2),
        (method, ("cbca","abcc"), 1),
        (method, ("abbcd","bcadb"), 3),
        (method, ("abccaacceecdeea","bcaacceeccdeaae"), 9),
        (method, ("fffeaacbdbdafcfbbafb","abcbdfafffefabdbbafc"), 10),
        (method, ("abccab","abccab"), 0),
        (method, ("abcdeabcdeabcdeabcde","aaaabbbbccccddddeeee"), 8),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))