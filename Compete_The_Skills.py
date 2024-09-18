#!/usr/bin/python3


def scores(arr1, arr2):
    """Returns comparisson result"""
    result = [0, 0]
    for skill in range(len(arr1)):
        if arr1[skill] > arr2[skill]:
            result[0] += 1
        elif arr2[skill] > arr1[skill]:
            result[1] += 1

    return result


if __name__ == "__main__":
    print(scores([4, 2, 7], [5, 6, 3]))
    print(scores([4, 2, 7], [5, 2, 8]))
