#!/usr/bin/python3
import math


def rectanglesInCircle(r):
    """
    Returns the number of rectangles you can fit in a circle of passed radius

    Variables naming:
        - res: The number of rectangles that fit inside.
        - d: Is the diameter of the circle.
        - h: Height of the rectangle.
    """
    res = 0
    # Start base. You can't fit a rectangle in a zero radius, dum dum.
    if r == 0:
        return 0
    d = 2 * r
    # Going through all possible heights
    for h in range(1, d + 1):
        # Calculates the maximum number of lengths that can fit in there.
        # This equation is derived from the fact that
        # you can not fit a rectangle whose
        # diagnoal is greates than the diameter of the circle in question.
        # You can google the formula for the diagnoal of a rectangle.
        res += int(math.sqrt(d ** 2 - h ** 2))
    return res


if __name__ == "__main__":
    print(rectanglesInCircle(2))
    print(rectanglesInCircle(3))
    print(rectanglesInCircle(4))
    print(rectanglesInCircle(16))
