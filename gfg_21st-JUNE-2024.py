#!/usr/bin/python3


def compareFrac(str):
    """Returns the greater of the two fractions"""
    nums = str.split(", ")
    first = int(nums[0].split("/")[0]) / int(nums[0].split("/")[-1])
    second = int(nums[-1].split("/")[0]) / int(nums[-1].split("/")[-1])
    if first > second:
        return nums[0]
    elif second > first:
        return nums[-1]
    else:
        return "equal"


if __name__ == "__main__":
    print(compareFrac("5/6, 11/45"))
    print(compareFrac("8/1, 8/1"))
    print(compareFrac("10/17, 9/10"))
