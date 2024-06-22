#!/usr/bin/python3
import re


def bracketNumbers(str):
    """
    Returns the 1-based index of brackets relative to the closing and opening
    """
    res = []
    temp = []
    bracket_number = 0
    for char in str:
        if char == "(":
            bracket_number += 1
            temp.append(bracket_number)
            res.append(bracket_number)
        elif char == ")":
            if temp:
                res.append(temp.pop())
    return res


if __name__ == "__main__":
    print(bracketNumbers("(aa(bdc))p(dee)"))
    print(bracketNumbers("(((()("))
    print(bracketNumbers("a(b)c(d)e(f)"))

