#!/usr/bin/python3


def binaryNextNumber(s):
    """Returns the next binary number after the passed one"""
    dec = int(s, 2)
    added = dec + 1
    return bin(added)[2:]


if __name__ == "__main__":
    print(binaryNextNumber("111"))
