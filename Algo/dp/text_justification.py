"""


"""

from math import pow

def cost(w, page_width):
    """
    calculate the cost of a line of words based on page width

    :param w:
    :param page_width:
    :return:
    """
    char_len = sum([len(i) for i in w]) + len(w) - 1      # character plus the spaces between words
    if char_len > page_width:
        return float("inf")
    else:
        return pow(page_width - char_len, 3)


def justify_text(w, page_width):
    """

    Justify the text based on minimizing the spaces. It is assumed no word is longer than page width

    :param w:
    :param page_width:
    :return:
    """
    n = len(w)
    c, p = [0] * (n+1), [0] * (n+1)

    c[n] = 0                # cost from the index described below to the end of the input word list
    p[n] = 0                # the index of the word immediately after the ending word of the first line

    for i in range(n-1, -1, -1):
        q = float("inf")
        for j in range(i+1, n+1):
            if q > cost(w[i:j], page_width) + c[j]:
                q = cost(w[i:j], page_width) + c[j]
                c[i] = q
                p[i] = j
    return c, p


def print_text(w, p, page_width):
    """

    :param w: a list of n words
    :param p: a list of indices of the word immediately after the ending word of the first line for various suffix of w
    :param page_width: page width
    :return: print the words in left justification with page width
    """
    i = 0
    while i < len(w):
        line = " ".join(w[i:p[i]]).ljust(page_width)
        print(line)
        i = p[i]

if __name__=="__main__":

    page_width = 16
    w = ["blah", "blah", "blah", "blah", "reallylongword"]
    p = [1,3,3,3,4]

    c, p = justify_text(w, page_width)
    print_text(w, p, page_width)

