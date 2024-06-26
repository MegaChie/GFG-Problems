#!/usr/bin/python3


def isToepliz(mat):
    """Returns 1 if the passed matrix is a Toeplitz matrix and 0 if not"""
    for raw in range(1, len(mat)):
        for col in range(1, len(mat[raw])):
            if (mat[raw][col] == mat[raw - 1][col - 1]):
                pass
            else:
                return 0
    return 1


if __name__ == "__main__":
    print(isToepliz([[6, 7, 8], [4, 6, 7], [1, 4, 6]]))
    print(isToepliz([[1 ,2 ,3], [4 ,5 ,6]]))
