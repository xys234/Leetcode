"""

93. Medium

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def dfs(start_index, curr_addr, groups):
            if start_index >= n or n - start_index < groups or n - start_index > 3 * groups:
                return

            if groups == 1:
                if start_index < n - 1 and s[start_index] == "0":
                    return
                elif int(s[start_index:]) <= 255:
                    ips.append(".".join(curr_addr + [s[start_index:]]))
                    return

            if s[start_index] == "0":
                dfs(start_index + 1, curr_addr + [s[start_index:start_index + 1]], groups - 1)
            else:
                for i in range(1, 4):
                    if int(s[start_index:start_index + i]) <= 255:
                        dfs(start_index + i, curr_addr + [s[start_index:start_index + i]], groups - 1)
            return

        n = len(s)
        ips = []
        if n >= 4:
            dfs(0, [], 4)
        return ips


if __name__ == '__main__':

    sol = Solution()

    cases = [

        (sol.restoreIpAddresses, ("255255255255", ), ["255.255.255.255"]),
        (sol.restoreIpAddresses, ("25525511135", ), ["255.255.11.135", "255.255.111.35"]),
        (sol.restoreIpAddresses, ("0000", ), ["0.0.0.0"]),
        (sol.restoreIpAddresses, ("1111", ), ["1.1.1.1"]),
        (sol.restoreIpAddresses, ("010010", ), ["0.10.0.10","0.100.1.0"]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))