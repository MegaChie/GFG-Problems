#!/usr/bin/python3
import math


def isPowerofTwo(n : int ) -> bool:
    """Returns "True" if n is a power of two and "False" if not"""
    # Making sure n is passed and is not 0
    if n and n != 0:
        return ((n & (n - 1)) == 0)


if __name__ == "__main__":
    print(isPowerofTwo(8))
    print(isPowerofTwo(98))
    print(isPowerofTwo(1))
    print(isPowerofTwo(549755813888))
