#!/usr/bin/python3


def padovanSequence(n):
    """Returns the nth number of the Padovan Sequence"""
    modu = 10**9 + 7
    sqance = [1, 1, 1]
    if n in [0, 1, 2]:
        return 1
    for num in range(3, n + 1):
        temp = sqance[num - 2] + sqance[num - 3]
        sqance.append(temp)
    return sqance[-1] % modu


if __name__ == "__main__":
    print(padovanSequence(3))
    print(padovanSequence(4))
    print(padovanSequence(20))
    print(padovanSequence(193))
