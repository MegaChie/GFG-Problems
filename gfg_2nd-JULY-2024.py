#!/usr/bin/python3


def subArraySum(arr, n, s):
    """Returns the left and right 1-based index of a subarray adding up to s"""
    # Not commplete. Some casses return the wrong output
    end =  start = count = 0

    while True:
        if count < s and end < n:
            count += arr[end]
            end += 1
        elif count == s:
            return [start + 1, end]
        elif count > s or end == n:
            count -= arr[start]
            start += 1
        if start == n:
            break

    return [-1]


if __name__ == "__main__":
    print(subArraySum([1, 2, 3, 7, 5], 5, 12))
    print(subArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 15))
    print(subArraySum([7, 2, 1], 3, 2))
    print(subArraySum([5, 3, 4], 3, 2))
    print(subArraySum([1, 0], 2, 0))
    print(subArraySum([1 ,2 ,3 ,4], 4, 0))
