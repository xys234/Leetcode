"""
224. Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.


"""

from typing import List, Tuple


class Solution:

    precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2
    }

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        prec = {
            "+":2,
            "-":2,
            "*":3,
            "/":3
        }

        operands = []
        operators = []
        input_stack = self.tokenize(s)

        for c in input_stack:
            if c.isdigit():
                operands.insert(0, c)
            elif c in "+-*/":
                if operators:
                    while operators and operators[0] in prec and prec[c] <= prec[operators[0]]:
                        op = operators.pop(0)
                        n2, n1 = operands.pop(0), operands.pop(0)
                        operands.insert(0, self.do_math(n1, n2, op))
                    operators.insert(0, c)
                elif not operators:
                    operators.insert(0, c)
            elif c == "(":
                operators.insert(0, c)
            elif c == ")":
                op = operators.pop(0)
                while op != "(":
                    n2, n1 = operands.pop(0), operands.pop(0)
                    operands.insert(0, self.do_math(n1, n2, op))
                    op = operators.pop(0)
            else:
                op = operators.pop(0)
                n2, n1 = operands.pop(0), operands.pop()
                operands.insert(0, self.do_math(n1, n2, op))

        while operators:
            op = operators.pop(0)
            n2, n1 = operands.pop(0), operands.pop(0)
            operands.insert(0, self.do_math(n1, n2, op))
        return int(operands[0])

    def tokenize(self, s):
        res = []
        temp = ""
        for c in s.replace(" ",""):
            if c not in "+-*/()":
                temp += c
            else:
                if temp:
                    res.append(temp)
                res.append(c)
                temp = ""
        if temp:
            res.append(temp)
        return res

    def do_math(self, n1, n2, oper):
        if oper == "+":
            return int(n1) + int(n2)
        elif oper == "-":
            return int(n1) - int(n2)
        elif oper == "*":
            return int(n1) * int(n2)
        else:
            return int(n1) // int(n2)

    def to_postfix(self, s):
        prec = {
            "+":1,
            "-":1,
            "*":2,
            "/":2
        }
        input_stack = self.tokenize(s)
        oper_stack = []
        postfix = []
        while input_stack:
            token = input_stack.pop(0)
            if token not in "+-*/()":
                postfix.append(token)
            elif token == "(":
                oper_stack.insert(0,token)
            elif token == ")":
                while oper_stack[0] != "(":
                    token = oper_stack.pop(0)
                    postfix.append(token)
                oper_stack.pop(0)
            else:
                token_prec = prec[token]
                while oper_stack and oper_stack[0] in prec and prec[oper_stack[0]] >= token_prec:
                    postfix.append(oper_stack.pop(0))
                oper_stack.insert(0,token)
        while oper_stack:
            postfix.append(oper_stack.pop(0))
        return postfix

    def tokenize2(self, s: str):
        s = s.replace(" ", "")

        tokens = []
        stack = []

        for c in s:
            if c not in self.precedence and c not in ("(", ")"):
                stack.append(c)
            else:
                if (c in self.precedence or c == ")") and stack:
                    tokens.append("".join(stack))
                    stack.clear()
                tokens.append(c)

        if stack:
            tokens.append("".join(stack))
        return tokens

    def to_postfix2(self, tokens: List[str]):
        stack = []
        postfix = []
        for token in tokens:
            if token not in ("(", ")") and token not in self.precedence:
                postfix.append(token)
            elif token == "(":
                stack.append(token)
            elif token in self.precedence:
                if not stack:
                    stack.append(token)
                else:
                    while stack and stack[-1] in self.precedence and \
                            self.precedence[stack[-1]] >= self.precedence[token]:
                        postfix.append(stack.pop(-1))
                    stack.append(token)
            else:
                while stack and stack[-1] != "(":
                    postfix.append(stack.pop(-1))
                stack.pop(-1)
        while stack:
            postfix.append(stack.pop(-1))
        return postfix

    def evaluate(self, operand: Tuple[float], operator: str):
        n1, n2 = float(operand[0]), float(operand[1])
        if operator == '+':
            return n1 + n2
        elif operator == '-':
            return n1 - n2
        elif operator == '*':
            return n1 * n2
        else:
            return n1 * 1.0 / n2

    def calculate2(self, s):
        tokens = self.tokenize2(s)
        postfix = self.to_postfix2(tokens)
        stack = []

        for token in postfix:
            if token not in self.precedence:
                stack.append(int(token))
            else:
                n2, n1 = stack.pop(-1), stack.pop(-1)
                stack.append(self.evaluate((n1, n2), token))
        return stack[-1]

    def calculate_solution(self, s):
        res, num, sign, stack = 0, 0, 1, []
        for ss in s:
            if ss.isdigit():
                num = num*10+int(ss)
            elif ss in ["-", "+"]:
                res += sign*num
                num = 0
                sign = [-1, 1][ss == '+']
            elif ss == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif ss == ")":
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num*sign


if __name__ == '__main__':
    sol = Solution()
    method = sol.calculate2
    # cases = [
    #     ('3 + 4', 7),
    #     ('2+(6-3)*2', 8),
    #     ("2147483647", 2147483647),
    #     (" 2-1 + 2 ", 3),
    #     ("0", 0),
    #
    # ]

    cases = [
        (method, ('3 + 4',), 7),
        (method, ('2+(6-3)*2',), 8),
        (method, ("2147483647",), 2147483647),
        (method, (" 2-1 + 2 ",), 3),
        (method, ("0",), 0),
        (method, ("46 -32 + 7",), 21),

    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))

