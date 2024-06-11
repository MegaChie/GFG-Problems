#!/usr/bin/python3
from typing import List


def maxTip(n: int, x: int, y: int, arr: List[int], brr: List[int]) -> int:
    """Returns a road map to get the maximum tip possiple"""
    differences = []
    for pos in range(n):
        diff = arr[pos] - brr[pos]
        differences.append((diff, pos))
    differences.sort(key=lambda x: abs(x[0]), reverse=True)
    total = 0
    tipA = 0
    tipB = 0
    for diff, pos in differences:
        if tipA < x and (tipB >= y or arr[pos] >= brr[pos]):
            total += arr[pos]
            tipA += 1
        elif tipB < y and (tipA >= x or arr[pos] < brr[pos]):
            total += brr[pos]
            tipB += 1
    return total


if __name__ == "__main__":
    print(maxTip(5, 3, 3, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
    print(maxTip(8, 4, 4, [1, 4, 3, 2, 7, 5, 9, 6], [1, 2, 3, 6, 5, 4, 9, 8]))
    print(maxTip(7, 3, 4,
                 [8, 7, 15, 19, 16, 16, 18], [1, 7, 15, 11, 12, 31, 9]))
    print(maxTip(5, 3, 3, [10, 4, 8, 6, 2], [7, 9, 5, 0, 0]))
