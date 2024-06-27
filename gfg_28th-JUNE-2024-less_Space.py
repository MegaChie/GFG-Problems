#!/usr/bin/python3


def pattern(arr):
    """
    Returns the first palindrome in matrix favouring rows over columns
    or -1 when none are found.
    """
    n = m = len(arr)
    # Check rows first
    for row in range(n):
        left, right = 0, m - 1
        while left < right:
            if arr[row][left] != arr[row][right]:
                break
            left += 1
            right -= 1
        if left >= right:
            return "{} R".format(row)

    # Check columns
    for col in range(m):
        top, bottom = 0, n - 1
        while top < bottom:
            if arr[top][col] != arr[bottom][col]:
                break
            top += 1
            bottom -= 1
        if top >= bottom:
            return "{} C".format(col)

    # No palindrome found
    return -1


if __name__ == "__main__":
    print(pattern([[1, 0, 0], [0, 1, 0], [0, 1, 0]]))
    print(pattern([[1, 0, 0], [0, 1, 0], [1, 1, 0]]))
    print(pattern([[1, 0],[1, 0]]))
