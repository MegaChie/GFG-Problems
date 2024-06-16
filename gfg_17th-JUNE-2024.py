#!/usr/bin/python3


def doIntersect(p1, q1, p2, q2):
    """Returns True if lines intersect or False if they do not"""
    x1, y1 = p1
    x2, y2 = q1
    x3, y3 = p2
    x4, y4 = q2

    deltax1 = x2 - x1
    deltay1 = y2 - y1
    deltax2 = x4 - x3
    deltay2 = y4 - y3

    dvidr = (deltax1 * deltay2) - (deltay1 * deltax2)
    if dvidr == 0:
        return "false"

    meetx = (((x3 - x1) * deltay2) - ((y3 - y1) * deltax2)) / dvidr
    meety = (((x3 - x1) * deltay1) - ((y3 - y1) * deltax1)) / dvidr
    if (0 <= meetx <= 1) and (0 <= meety <= 1):
        return "true"
    return "false"


if __name__ == "__main__":
    print(doIntersect([1, 1], [10, 1], [1, 2], [10, 2]))
    print(doIntersect([10, 0], [0, 10], [0, 0], [10, 10]))
    print(doIntersect([5, -2], [13, 2], [2, -3], [3, 0]))
