#!/usr/bin/python3
from itertools import combinations


def countPairsWithDiffK(arr, k):
    """Finds the number of pairs of integers whose difference equals k"""
    if len(arr) > 1 and k:
        comb = combinations(arr, 2)
        # return list(comb)

        res = 0
        for tup in comb:
            if (abs(tup[1] - tup[0])) == k:
                res += 1
        return res
    
    return 0


if __name__ == "__main__":
    print(countPairsWithDiffK([1, 5, 3, 4, 2], 3))
    print(countPairsWithDiffK([8, 12, 16, 4, 0, 20], 4))
