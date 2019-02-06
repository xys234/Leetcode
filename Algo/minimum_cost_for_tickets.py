"""

983.

In a country popular for train travel, you have planned some train travelling one year in advance.
The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2,
then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.



Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.


"""

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """

        dp = [0] * (days[-1]+1)         # dp[i] is the minimum cost of travel from 1st to the ith day
        dp[0] = 0

        current_day = 1
        for d in days:
            while current_day <= d - 1:
                dp[current_day] = dp[current_day - 1]
                current_day += 1
            if current_day == d:
                if current_day >= 30:
                    dp[current_day] = min(dp[current_day-30]+costs[2], dp[current_day-7]+costs[1],
                                          dp[current_day-1]+costs[0])
                elif current_day >= 7:
                    dp[current_day] = min(dp[current_day - 7] + costs[1],
                                          dp[current_day - 1] + costs[0], costs[2])
                else:
                    dp[current_day] = min(dp[current_day - 1] + costs[0], costs[1], costs[2])
                current_day += 1
        return dp[-1]

if __name__=='__main__':

    sol = Solution()

    cases = [

        # (sol.mincostTickets, ([1,4,6,7,8,20], [2,7,15]), 11),
        # (sol.mincostTickets, ([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]), 17),
        # (sol.mincostTickets, ([1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29], [3,14,50]), 50),
        (sol.mincostTickets, ([1,2,4,5,6,9,10,12,14,15,18,20,21,22,23,24,25,26,28], [3,13,57]), 45),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))