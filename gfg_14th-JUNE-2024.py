#!/usr/bin/python3


def armstrongNumber (n):
    """Returns Yes if passed number is an Armstrong number, No if it isn't"""
    digits = [int(x) for x in str(n)]
    digits = [x ** 3 for x in digits]
    if sum(digits) == n:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    print(armstrongNumber(153))
    print(armstrongNumber(372))
