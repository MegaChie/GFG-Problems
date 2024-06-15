#!/usr/bin/python3


def kthSmallest(arr, l, r, k):
    """
    Returns the kth smallest number in the list

    Vairables names:
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
    """
    arr.sort(reverse=True)
    return arr[-k]


if __name__ == "__main__":
    print(kthSmallest([7, 10, 4, 3, 20, 15], 0, 5, 3))
    print(kthSmallest([7, 10, 4, 20, 15], 0, 4, 4))
