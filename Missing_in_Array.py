#!/usr/bin/python3


def rearrange(n, arr):
    """Returns the missing number in an array"""
    expected_array = list(range(1, n + 1))
    return sum(expected_array) - sum(arr)


if __name__ == "__main__":
    print(rearrange(5, [1, 2, 3, 5]))
    print(rearrange(2, [1]))
