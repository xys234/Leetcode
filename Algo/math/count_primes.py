from math import ceil, sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        if n == 3:
            return 1

        primes = [2]
        for i in range(3, n, 2):
            if self.is_prime(i, primes):
                primes.append(i)
        return len(primes)

    @staticmethod
    def is_prime(k, primes):
        for prime in primes:
            if k % prime == 0:
                return False
            if prime > ceil(sqrt(k)):
                break
        return True

    def countPrimes2(self, n):
        if n <= 2:
            return 0

        res = [True] * n
        res[0] = res[1] = False

        for p in range(2, ceil(sqrt(n)), 1):
            if res[p]:
                for i in range(p * 2, n, p):
                    res[i] = False

        return sum(res)


if __name__ == '__main__':
    sol = Solution()
    method = sol.countPrimes2

    cases = [
        (method, (10, ), 4),
        (method, (0, ), 0),
        (method, (1, ), 0),
        (method, (2, ), 0),
        (method, (3, ), 1),
        (method, (4, ), 2),
        (method, (20, ), 8),
        (method, (40, ), 12),
        (method, (50, ), 15),
        (method, (10000, ), 1229),
        (method, (499979, ), 41537),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))