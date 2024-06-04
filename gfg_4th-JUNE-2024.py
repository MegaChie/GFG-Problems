#!/usr/bin/python3


def binaryNextNumber(s):
    """Returns the next binary number after the passed one"""
    dec = 0
    exp = 0
    for char in s[::-1]:
        dec += int(char) * (2 ** exp)
        exp += 1
    res = str(bin(dec + 1))
    return res[2::]


if __name__ == "__main__":
    print(binaryNextNumber("111"))
