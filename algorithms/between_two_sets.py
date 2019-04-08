#!//bin/python3

"""
Given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

    1. The elements of the first array are all factors of the integer being considered
    2. The integer being considered is a factor of all elements of the second array

    Given a[i], b[j] find x's such that x%a[i] = 0 and b[j]%x = 0
"""


def getX(a, b):
    """
    brute force solution
    """

    # O (2n)
    a_max = max(a)
    b_min = min(b)

    X1 = []

    # worst case O(n*k)
    for i in range(a_max, b_min+1, 1):
        accept = True
        for j in a:
            if not i % j == 0:
                accept = False
                break
        if accept:
            X1.append(i)

    # worst case O(m*k)
    X = []

    for i in X1:
        accept = True
        for j in b:
            if not j % i == 0:
                accept = False
                break
        if accept:
            X.append(i)

    return len(X)


if __name__ == "__main__":
    a = [3, 4]
    b = [24, 48]

    c = [2, 4]
    d = [16, 32, 96]

    e = [1]
    f = [100]

    print(getX(a, b))
    print(getX(c, d))
    print(getX(e, f))
