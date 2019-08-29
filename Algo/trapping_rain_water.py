"""

42.
Hard

"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # find all the traps
        dec, inc, stack = False, False, [-float('inf')]
        for h in height:
            if not dec and not inc:
                if h < stack[-1]:
                    dec = True
                    stack.append(h)
                elif h == stack[-1]:
                    stack.append(h)
                else:
                    stack.pop()
                    stack.append(h)

            elif





    @staticmethod
    def store_water(group):
        low = min(group[0], group[-1])
        water = 0
        for i in range(1, len(group)-1):
            water += (low-group[i])
        return water



if __name__ == '__main__':
    sol = Solution()

    print(sol.store_water([1, 0, 2]))
    print(sol.store_water([2,1,0,1,3]))
    print(sol.store_water([3,2,1,2]))

    # method = sol.trap
    #
    # cases = [
    #     (method, ([0,1,0,2,1,0,1,3,2,1,2,1],), 6),
    # ]
    #
    # for i, (func, case, expected) in enumerate(cases):
    #     ans = func(*case)
    #     if ans == expected:
    #         print("Case {:d} Passed".format(i + 1))
    #     else:
    #         print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))

