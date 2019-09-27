"""


"""


class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """

        unique = 0
        chars = [[] for _ in range(26)]
        for i, c in enumerate(text):
            ind = ord(c) - ord('a')
            if not chars[ind]:
                unique += 1
            chars[ind].append(i)

        print([c for c in chars if len(c) > 0])

        visited = [False] * 26

        def dfs(visited, start, curr):
            if len(curr) == unique:
                return True

            elif start >= len(text):
                return False

            for j, char in enumerate(chars):
                if char and not visited[j]:
                    visited[j] = True
                    for k in char:
                        if k >= start:
                            curr.append(chr(ord('a')+j))
                            if dfs(visited, k+1, curr):
                                return True
                            else:
                                curr.pop()
                    visited[j] = False
            return False

        ans = []
        dfs(visited, 0, ans)
        return ''.join(ans)


if __name__ == '__main__':

        sol = Solution()
        method = sol.smallestSubsequence

        cases = [

            # (method, ("leetcode",), "letcod"),
            (method, ("abcd",), "abcd"),

        ]

        for k, (func, case, expected) in enumerate(cases):
            ans = func(*case)
            if ans == expected:
                print("Case {:d} Passed".format(k + 1))
            else:
                print("Case {:d} Failed; Expected {:s} != Output {:s}".format(k + 1, str(expected), str(ans)))