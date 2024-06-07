#!/usr/bin/python3


def findExtra(n,a,b):
    """
    Returns the extra element index of the first array
    """
    for i in range(len(b)):
        if a[i] != b[i]:
            return i
    return len(a) - 1


if __name__ == "__main__":
    print(findExtra(7, [2,4,6,8,9,10,12], [2,4,6,8,10,12]))
    print(findExtra(6, [3,5,7,8,11,13], [3,5,7,11,13]))
    print(findExtra(2, [11, 2], [11]))
