#!/usr/bin/python3


def subArraySum(arr, n, s):
    """Returns the left and right 1-based index of a subarray adding up to s"""
    if s == 0 and 0 not in arr:
        return [-1]
    if s in arr:
        return [arr.index(s) + 1, arr.index(s) + 1]

    start = 0
    count = 0
    for end in range(n):
        count += arr[end]

        while count > s and start <= end:
            count -= arr[start]
            start += 1

        if count == s:
            return [start + 1, end + 1]

    return [-1]


if __name__ == "__main__":
    print(subArraySum([1, 2, 3, 7, 5], 5, 12))
    print(subArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 15))
    print(subArraySum([7, 2, 1], 3, 2))
    print(subArraySum([5, 3, 4], 3, 2))
    print(subArraySum([1, 0], 2, 0))
    print(subArraySum([1 ,2 ,3 ,4], 4, 0))
