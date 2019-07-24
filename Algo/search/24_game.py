"""
679. 24 Game (Hard)

You have 4 cards each containing a number from 1 to 9.
You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division.
For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator.
For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.

Review
2019.02.06 backtracking and recursion

"""


from operator import add, sub, mul, truediv

class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return abs(nums[0]-24) < 1e-6
        ops = [add, sub, mul, truediv]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:      # a number can only be used once
                    continue
                next_nums = [nums[k] for k in range(len(nums)) if i != k != j]  # numbers except nums[i] and nums[j]
                for op in ops:
                    if ((op is add or op is mul) and j > i) \
                            or (op == truediv and nums[j] == 0):  # add and mul are commutative;
                        continue
                    next_nums.append(op(nums[i], nums[j]))
                    if self.judgePoint24(next_nums):              # recursion
                        return True
                    next_nums.pop()
        return False

    @staticmethod
    def permutations(iterable, r=None):
        # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
        # permutations(range(3)) --> 012 021 102 120 201 210
        pool = tuple(iterable)
        n = len(pool)
        r = n if r is None else r
        if r > n:
            return
        indices = list(range(n))
        cycles = list(range(n, n - r, -1))
        yield tuple(pool[i] for i in indices[:r])
        while n:
            for i in reversed(range(r)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i + 1:] + indices[i:i + 1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    yield tuple(pool[i] for i in indices[:r])
                    break
            else:
                return

    def judgePoint24_v2(self, nums):
        return self.calculate_target(nums, 24)

    def calculate_target(self, nums, target):
        n = len(nums)
        if n == 1:
            return abs(nums[0]-target) < 1e6

        perms = self.permutations(range(len(nums)))
        res = False
        for perm in perms:
            for oper in [add, sub, mul]:
                new_num = oper(nums[perm[0]], nums[perm[1]])
                next_nums = [new_num] + nums[2:]
                res = self.calculate_target(next_nums, target)
                if res:
                    return res
            if not res and nums[perm[1]] != 0:
                new_num = oper(nums[perm[0]], nums[perm[1]])
                next_nums = [new_num] + nums[2:]
                res = self.calculate_target(next_nums, target)
        return res


if __name__ == "__main__":
    sol = Solution()

    nums = [4,1,8,7]
    print(sol.permutations(nums))
    # print(sol.judgePoint24_v2(nums))
