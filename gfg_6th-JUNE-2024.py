#!/usr/bin/python3


def maxSubArraySum(arr, n):
    """Returns the maximum sum of a contiguous sub-array"""
    maxFound = float('-inf')
    maxAtEnd = 0
    for pos in range(n):
        maxAtEnd += arr[pos]
        if maxFound < maxAtEnd:
            maxFound = maxAtEnd
        if maxAtEnd < 0:
            maxAtEnd = 0
    return maxFound


if __name__ == "__main__":
    print(maxSubArraySum([1, 2, 3, -2, 5], 5))
    print(maxSubArraySum([-1, -2, -3, -4], 4))
    print(maxSubArraySum([5, 4, 7], 3))
    print(maxSubArraySum([-10, -2, -3, -4], 4))

