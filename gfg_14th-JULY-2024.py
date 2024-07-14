#!/usr/bin/python3


def segregate0and1(arr):
    """
    Separates 0s and 1s and puts the 1s to the right of the array
    then returns the separated array.
    """
    if arr:
        arr.sort()
        return arr
    else:
        return


if __name__ == "__main__":
    print(segregate0and1([0, 0, 1, 1, 0]))
    print(segregate0and1([1, 1, 1, 1]))
    print(segregate0and1([]))
    print(segregate0and1([0, 0, 0, 0]))
