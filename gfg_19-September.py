#!/usr/bin/python3


def reverseWords(str):
    """Reverse words of string and returns it"""
    words = str.split(".")
    words = words[::-1]
    return ".".join(words)


if __name__ == "__main__":
    print(reverseWords("i.like.this.program.very.much"))
    print(reverseWords("pqr.mno"))
