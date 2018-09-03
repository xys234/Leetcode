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

class Solution:
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


if __name__ == '__main__':
    sol = Solution()
    cases = [
        ('3 + 4', 7),
        ('2+(6-3)*2', 8),
        ("2147483647", 2147483647),
        (" 2-1 + 2 ", 3),
        ("0", 0),

    ]
    # print(sol.calculate(cases[0][0]))
    # print(sol.calculate(cases[1][0]))
    # print(sol.calculate(cases[2][0]))
    # print(sol.calculate(cases[3][0]))
    print(sol.calculate(cases[4][0]))