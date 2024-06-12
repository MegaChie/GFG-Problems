#!/usr/bin/python3
from typing import List


def majorityElement(A: List[int], N: int) -> int:
    """Returns the majority element of a list"""
    major = None
    cwnt = 0
    for num in A:
        if cwnt == 0:
            major = num
        if num == major:
            cwnt += 1
        else:
            cwnt -= 1
    if A.count(major) > N / 2:
        return major
    else:
        return -1


if __name__ == "__main__":
    print(majorityElement([1, 2, 3], 3))
    print(majorityElement([3, 1, 3, 3, 2], 5))
