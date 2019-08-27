from math import gcd


def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return str(0)
    if numerator < 0 and denominator > 0:
        return '-' + fractionToDecimal(-numerator, denominator)
    if numerator > 0 and denominator < 0:
        return '-' + fractionToDecimal(numerator, -denominator)

    if numerator % denominator == 0:
        return str(int(numerator / denominator))

    g = gcd(numerator, denominator)
    n, d = int(numerator/g), int(denominator/g)
    integer = str(n // d)
    n = n % d

    i, fraction, remainder, repeat = 0, [], {}, -1
    remainder[n] = i
    while True:
        n = n * 10
        f = n // d
        n = n - f * d
        fraction.append(str(f))
        i += 1

        if n == 0:
            break
        else:
            if n in remainder:
                repeat = remainder[n]
                break
            else:
                remainder[n] = i

    if repeat < 0:
        return integer + '.' + ''.join(fraction)
    else:
        p1 = ''.join(fraction[:repeat])
        return integer + '.' + p1 + '(' + ''.join(fraction[repeat:]) + ')'


# print(fractionToDecimal(45, 56))
# print(fractionToDecimal(2, 3))
# print(fractionToDecimal(2, 4))
# print(fractionToDecimal(4, 333))
# print(fractionToDecimal(1, 6))
print(fractionToDecimal(0, 3))