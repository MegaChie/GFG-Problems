#!/usr/bin/python3


def rotatematrix(k, mat):
    """
    Returns the passed matrix after rotating it k times.
    This is done by slicing a number of elements that
    are equal to the numbers of rotates, then put that slice to the left.

    Variables naming:
    - mat: The matrix to rotate.
    - k: Number of shifts to be done.
    - res: The matrix after rotating.
    - cut: The number elements to cut in each row, or
           to take and add it to the start if you may.
    """
    res = []
    # No turns
    if k == 0:
        return mat
    # 1-dimentional array
    if (str(mat).count("[") == 1 and
       str(mat).count("[") == 1):
        n = len(mat)
        cut = k % n
        res.append(mat[cut:] + mat[:cut])
        return res
    # 2-dimentional array
    for raw in mat:
        n = len(raw)
        cut = k % n
        res.append(raw[cut:] + raw[:cut])
    return res


if __name__ == "__main__":
    print(rotatematrix(1, [[1 ,2 ,3], [4, 5, 6], [7, 8, 9]]))
    print(rotatematrix(0, [[1 ,2 ,3], [4, 5, 6], [7, 8, 9]]))
    print(rotatematrix(2, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(rotatematrix(2, [1, 2, 3, 4]))
