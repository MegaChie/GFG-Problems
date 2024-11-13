#!/usr/bin/python3
import sys


def minSum(arr):
    """
    Finds the minimum possible sum of two numbers
    formed using the elements of the array
    """
    sys.set_int_max_str_digits(524288)
    if len(arr) == 1:
        return arr[0]
    elif sum(arr) == 0:
        return "0"
    
    arr.sort()
    res, res2 = "", ""

    for num in range(len(arr)):
        if num % 2 == 0:
            res += str(arr[num])
        else:
            res2 += str(arr[num])
    
    return str(int(res) + int(res2)).lstrip("0")


if __name__ == "__main__":
    print(minSum([6, 8, 4, 5, 2, 3]))
    print(minSum([5, 3, 0, 7, 4]))
    print(minSum([9, 4]))
    print(minSum([5]))
