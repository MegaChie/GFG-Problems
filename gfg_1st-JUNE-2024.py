#!/usr/bin/python3
def Solution(s):
    freq = {}
    alpha = []
    post = {}
    x = 0
    y = 0

    # Pre-processing the string
    s = s.strip().replace(" ", "").casefold()
    # Calculate frequancey of each leter
    for elem in s:
        freq[elem] = freq.get(elem, 0) + 1
    print(freq)

    # Calculate the position in alphabet
    for count in range(97, 123):
        alpha.append(chr(count))
    for elem in freq.keys():
        post[elem] = alpha.index(elem) + 1
    print(post)

    # Calculate x and y
    for elem in freq.keys():
        if (freq[elem] % 2 == 0 and
            post[elem] % 2 == 0):
            x = x + 1
        elif (freq[elem] % 2 != 0 and
              post[elem] % 2 != 0):
            y = y + 1
        else:
            pass
    print("x = {}\ny = {}".format(x, y))

    # Final result
    if (y + x) % 2 == 0:
        return "EVEN"
    else:
        return "ODD"


if __name__ == "__main__":
    print(Solution("meGa"))
