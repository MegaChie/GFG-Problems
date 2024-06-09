#!/usr/bin/python3


def matchPairs(n, nuts, bolts):
    """Returns the passed arrays in the correct order"""
    nuts.sort()
    bolts.sort()
    return nuts, bolts


if __name__ == "__main__":
    print(matchPairs(5, ["@", "%", "$", "#", "^"], ["%", "@", "#", "$", "^"]))
    print(matchPairs(9, ["^", "&", "%", "@", "#", "*", "$", "?", "!"],
                     ["?", "#", "@", "%", "&", "*", "$", "^", "!"]))
