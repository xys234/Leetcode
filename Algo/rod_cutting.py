"""
Given a rod of length n inches and a table of prices pi for i = 1; 2; : : : ; n,
determine the maximum revenue rn obtainable by cutting up the rod and selling the pieces.



"""


def cut_rod(l, prices):
    """

    :param l: int, length of the rod
    :param prices: a dict (length, price)
    :return:  r, cuts
    """

    r = [0 for i in range(l+1)]
    cuts = [0 for i in range(l+1)]

    r[0] = 0
    for j in range(1,l+1):
        q = -float("inf")
        for i in range(1,j+1):
            if prices[i] + r[j-i] > q:
                q = prices[i] + r[j-i]
                cuts[j] = i
        r[j] = q
    return (r[l], cuts)


def print_rod_cut(l, cuts):
    while l > 0:
        print(str(cuts[l])+",")
        l -= cuts[l]



if __name__=="__main__":
    prices = [
        (1, 1),
        (2, 5),
        (3, 8),
        (4, 9),
        (5, 10),
        (6, 17),
        (7, 17),
        (8, 20),
        (9, 24),
        (10,30)
    ]
    prices = dict(prices)
    l = 7
    r, cuts = cut_rod(l, prices)
    print("Maximum revenue {0:.0f}".format(r))
    print_rod_cut(l, cuts)






