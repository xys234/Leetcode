"""
739. Daily Temperatures

Given a list of daily temperatures T, return a list such that, for each day in the input,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].

"""

class Solution:
    def dailyTemperatures(self, T):
        """


        :param T:
        :return:


        Maintain the hottest and closest temperature up to this day in a stack.
        if a day is father and cooler, it is removed since one can find a hotter and closer day
        Iterate backwards

        """
        ans = [0] * len(T)
        stack = [] #indexes from hottest to coldest
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans

    def dailyTemperatures2(self, T):
        days = [0]*len(T)

        stack = []
        for i, t in enumerate(T):
            while stack and t > stack[-1][1]:
                top = stack.pop()
                days[top[0]] = i - top[0]
            stack.append((i, t))
        return days


if __name__ == '__main__':

    sol = Solution()
    method = sol.dailyTemperatures2

    cases = [

        (method, ([73, 74, 75, 71, 69, 72, 76, 73],), [1, 1, 4, 2, 1, 1, 0, 0]),
             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))