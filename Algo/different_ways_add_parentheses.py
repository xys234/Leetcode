"""

Given a string of numbers and operators, return all possible results from computing all the different
possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10


"""

from operator import add, sub, mul, truediv


class Solution:
    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }

    def diffWaysToCompute(self, input):
        """

        :param input:
        :type input: str
        :return:
        :rtype list
        """

        mem = {}
        self.helper(input, mem)
        return mem[input]

    @staticmethod
    def is_operator(ch):
        """
        Check if a character is an operator
        :param ch: a string with length 1
        :type ch: str
        :return:
        """

        return ch in {"+", "-", "*"}

    def helper(self, s, mem):
        """

        :param s:
        :type s: str
        :param mem:
        :type mem: dict
        :return:
        """

        n = len(s)
        if s in mem:
            return mem[s]

        res = []
        res_prefix, res_suffix, operator_exists = [], [], False
        for j, ch in enumerate(s):
            if self.is_operator(ch) and j > 0:
                operator_exists = True
                res_prefix = self.helper(s[:j], mem)
                res_suffix = self.helper(s[j+1:], mem)

            # combine the prefix and suffix results
            for _, pre in enumerate(res_prefix):
                for _, suf in enumerate(res_suffix):
                    if s[j] == '+':
                        res.append(pre+suf)
                    elif s[j] == '-':
                        res.append(pre-suf)
                    elif s[j] == '*':
                        res.append(pre*suf)
        if not operator_exists:
            res.append(int(s))
        mem[s] = res
        return res

    def diffWaysToCompute_fast(self, input):
        """
        :type input: str
        :rtype: List[int]

        recursion then combine

        """
        ops = {"+": add, "-": sub, "*": mul, "/": truediv}
        res = []
        for k, c in enumerate(input):
            if c in ops and k > 0:
                left = self.diffWaysToCompute_fast(input[:k])
                right = self.diffWaysToCompute_fast(input[k+1:])
                res.extend([ops[c](a, b) for a in left for b in right])
        if res:
            return res
        else:
            return [int(input)]

    def diffWaysToCompute2(self, input):
        ops = self.find_operators(input)
        if len(ops) == 0:
            return [int(input)]

        res = []
        for ind, op in ops.items():
            s1, s2 = input[:ind], input[ind+1:]
            res1 = self.diffWaysToCompute2(s1)
            res2 = self.diffWaysToCompute2(s2)
            for r1 in res1:
                for r2 in res2:
                    if op == truediv and r2 == 0:
                        continue
                    res.append(op(r1, r2))
        return res

    def find_operators(self, s):
        res = {}
        for i, c in enumerate(s):
            if i == 0 and c == '-':
                continue
            if c in self.operators:
                res[i] = self.operators[c]
        return res


if __name__ == '__main__':

    sol = Solution()
    method = sol.diffWaysToCompute2

    cases = [

        (method, ("2-1-1", ), [0, 2]),
        (method, ("2*3-4*5", ), [-34, -14, -10, -10, 10]),
        (method, ("-2+3-2", ), [-1, -1]),
        (method, ("0", ), [0]),
        (method, ("11", ), [11]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if sorted(ans) == sorted(expected):
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))