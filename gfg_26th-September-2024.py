#!/usr/bin/python3


def maxStep(arr):
    """Return the number of the longest jump sequance possible in the array"""
    if arr:
        jump_count = 0
        temp = 0
        arr_lenght = len(arr)
        for elem in range(arr_lenght):
            # print(elem)
            if elem != arr_lenght - 1 and arr[elem] < arr[elem + 1]:
                temp += 1
                if temp > jump_count:
                    jump_count = temp
            if elem != arr_lenght - 1 and arr[elem] >= arr[elem + 1]:
                temp = 0
        return jump_count

    return 0


if __name__ == "__main__":
    print(maxStep([1, 2, 2, 3, 2]))
