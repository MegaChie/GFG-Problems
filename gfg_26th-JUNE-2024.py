#!/usr/bin/python3


def FindCoverage(matrix):
    """Returns the sum of coverage of all zeros in the matrix"""
    res = 0
    for raw in range(len(matrix)):
        for elem in range(len(matrix[raw])):
            if matrix[raw][elem] == 0:
                temp = 0
                if elem > 0 and matrix[raw][elem - 1] == 1:
                    temp += 1
                if elem < len(matrix[0]) - 1 and matrix[raw][elem + 1] == 1:
                    temp += 1
                if raw > 0 and matrix[raw - 1][elem] == 1:
                    temp += 1
                if raw < len(matrix) - 1 and matrix[raw + 1][elem] == 1:
                    temp += 1
                res += temp
    return res


if __name__ == "__main__":
    print(FindCoverage([[0, 1, 0], [0, 1, 1], [0, 0, 0]]))
    print(FindCoverage([[0, 1]]))
