#!/usr/bin/python3


def missingNumber(n, arr):
    """Returns the missing element in the array sequance"""
    realSum = n * (n + 1) // 2
    tempSum = sum(arr)
    return realSum - tempSum


if __name__ == "__main__":
    print(missingNumber(5, [1, 2, 3, 5]))
    print(missingNumber(2, [1]))
