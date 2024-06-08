#!/usr/bin/python3
from typing import List


def zigZag(n : int, arr : List[int]) -> None:
    """Turns the passed list into the Zig-Zag form"""
    for i in range(n - 1):
        if i % 2 == 0:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


if __name__ == "__main__":
    print(zigZag(7, [4, 3, 7, 8, 6, 2, 1]))
    print(zigZag(4, [1, 4, 2, 3]))
