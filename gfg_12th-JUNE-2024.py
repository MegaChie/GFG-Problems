#!/usr/bin/python3


def countNumberswith4(n : int) -> int:
    """Returns the number of integers containing 4 in them"""
    count = 0
    for num in range(1, n + 1, 1):
        if "4" in str(num):
            count += 1
    return count


if __name__ == "__main__":
    print(countNumberswith4(9))
    print(countNumberswith4(14))
    print(countNumberswith4(100))
