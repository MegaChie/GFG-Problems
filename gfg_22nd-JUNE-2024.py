#!/usr/bin/python3
import re


def ExtractNumber(sentence):
    """Returns the biggest number not containing 9"""
    nums = re.findall(r"[0-9]+", sentence)
    candid = []
    for num in nums:
        if re.search(r"9", num):
            pass
        else:
            candid.append(int(num))
    return max(candid) if len(candid) > 0 else -1
    

if __name__ == "__main__":
    print(ExtractNumber("This is alpha 5057 and 97"))
    print(ExtractNumber("Another input 9007"))
    print(ExtractNumber("This is alpha 5057 and 97, 5"))
    print(ExtractNumber("testing for: 4, 19, 20, 55 and 9"))
