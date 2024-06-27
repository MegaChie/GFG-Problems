#!/usr/bin/python3


def pattern(arr):
    """
    Returns the first palindrome in matrix favouring rows over columns
    or -1 when none are found.
    """
    note = str()
    index = int()
    # Check rows first
    for row in range(len(arr)):
        if arr[row] == arr[row][::-1]:
            note = "R"
            index = row
            return "{} {}".format(index, note)

    # Check columns
    for col in range(len(arr)):
        temp = list()
        for row in arr:
            temp.append(row[col])
        if temp == temp[::-1]:
            note = "C"
            index = col
            return "{} {}".format(index, note)
    return -1


if __name__ == "__main__":
    print(pattern([[1, 0, 0], [0, 1, 0], [0, 1, 0]]))
    print(pattern([[1, 0, 0], [0, 1, 0], [1, 1, 0]]))
    print(pattern([[1, 0],[1, 0]]))
