#!/usr/bin/python3


def sumMatrix(n, q):
    """Returns the number of q occurances in an array of size nXn"""
    if q > 2 * n:
        return 0
    return min(n, q - 1) - max(1, q - n) + 1


if __name__ == "__main__":
    print(sumMatrix(4, 7))
    print(sumMatrix(5, 4))
