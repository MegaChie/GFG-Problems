#!/usr/bin/python3
from collections import Counter


def countPairsWithDiffK(arr, k):
    """Finds the number of pairs of integers whose difference equals k"""
    if len(arr) > 1 and k:
        count = 0
        element_counts = Counter(arr)  # Count occurrences of each number

        for num in element_counts:
            if (num + k) in element_counts:
                count += element_counts[num] * element_counts[num + k]

        return count

    return 0


if __name__ == "__main__":
    print(countPairsWithDiffK([1, 5, 3, 4, 2], 3))
    print(countPairsWithDiffK([8, 12, 16, 4, 0, 20], 4))
