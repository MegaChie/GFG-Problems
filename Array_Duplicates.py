#!/usr/bin/python3
from typing import List


def duplicates(n: int, arr: List[int]) -> List[int]:
    """
    Returns the duplicates in an array in a ascending order.

    Args:
    - n: Length of the array to be processed.
    - arr: The array to find duplicates in.
    """
    if n and arr:
        frequancy = {}
        repeted = []

        for number in arr:
            frequancy[number] = frequancy.get(number, 0) + 1

        for number, count in frequancy.items():
            if count > 1:
                repeted.append(number)

        if not repeted:
            return [-1]

        repeted.sort()
        return repeted

    return [-1]


if __name__ == "__main__":
    print(duplicates(4, [0, 3, 1, 2]))
    print(duplicates(5, [2, 3, 1, 2, 3]))
