#!/usr/bin/python3


def sort012(arr,n):
    """Returns sorted array consisting of 0s, 1s and 2s"""
    arr.sort()
    return arr


if __name__ == "__main__":
    print(sort012([0, 2, 1, 2, 0], 5))
    print(sort012([0, 1, 0], 3))
