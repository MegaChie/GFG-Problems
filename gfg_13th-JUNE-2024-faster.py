#!/usr/bin/python3


def padovanSequence(n):
    """Returns the nth number of the Padovan Sequence"""
    modu = 10**9 + 7
    if n in [0, 1, 2]:
        return 1
    a, b, c = 1, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, (a + b) % modu
    return c


if __name__ == "__main__":
    print(padovanSequence(3))
    print(padovanSequence(4))
    print(padovanSequence(20))
    print(padovanSequence(193))
