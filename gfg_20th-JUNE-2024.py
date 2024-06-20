#!/usr/bin/python3


def InternalCount(p, q, r):
    """
    Returns the number of integeral lattice points found inside the triangle
    """
    res = 0
    boundX1, boundX2 = min(p[0], q[0], r[0]), max(p[0], q[0], r[0])
    boundY1, boundY2 = min(p[1], q[1], r[1]), max(p[1], q[1], r[1])

    for x in range(boundX1, boundX2 + 1):
        for y in range(boundY1, boundY2 + 1):
            d1 = (q[0] - p[0]) * (y - p[1]) - (q[1] - p[1]) * (x - p[0])
            d2 = (r[0] - q[0]) * (y - q[1]) - (r[1] - q[1]) * (x - q[0])
            d3 = (p[0] - r[0]) * (y - r[1]) - (p[1] - r[1]) * (x - r[0])
            if (d1 > 0 and d2 > 0 and d3 > 0) or (d1 < 0 and d2 < 0 and d3 < 0):
                res += 1
    return res


if __name__ == "__main__":
    print(InternalCount([0, 0], [0, 5], [5, 0]))
    print(InternalCount([62, -3], [5, -45], [-19, -23]))
