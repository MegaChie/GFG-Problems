#!/usr/bin/python3
import math


def armstrongNumber(n):
    """Returns Yes if passed number is an Armstrong number, No if it isn't"""
    summed = 0
    temp = n
    dgitsCwnt = math.floor(math.log(n, 10)) + 1
    while n != 0:
        summed += (n % 10) ** dgitsCwnt
        n //= 10
    if summed == temp:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    print(armstrongNumber(153))
    print(armstrongNumber(372))
    print(armstrongNumber(123456))
    print(armstrongNumber(5892))
