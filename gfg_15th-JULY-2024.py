#!/usr/bin/python3


def smallestNumber(s, d):
    """
    Returns a numirical string that have d number of digits
    and s as the sum of those digits.

    Variables:
    - res: Result to be returned.
    """
    # Making sure such combination exists
    if 9 * d >= s:
        # So we do not start with a number whose first digit is 0
        s -= 1
        # Array with length egual to number of digits
        res = [0] * d
        i = -1
        # Start from the right most element and stop at the other end
        while i != -d - 1:
            res[i] = min(9, s)
            # Subtract element from the total sum
            s -= res[i]
            i -= 1
        # Adds back the 1 we took at the start
        res[0] += 1
        # Return the list as a string
        return "".join(map(str, res))
    return -1


if __name__ == "__main__":
    print(smallestNumber(18, 4))
    print(smallestNumber(27, 4))
    print(smallestNumber(9, 2))
    print(smallestNumber(20, 3))
    print(smallestNumber(40, 5))
    print(smallestNumber(18, 2))
    print(smallestNumber(00, 1))
    print(smallestNumber(1, 0))
