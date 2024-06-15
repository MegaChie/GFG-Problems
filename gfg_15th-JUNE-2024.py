#!/usr/bin/python3


def getCount(n):
    """
    Returns possible unique sequences of length n that you can create
    by pressing buttons on the phone and
    only directly up, left, right, or down from it.
    """
    transitions = {1: [1, 2, 4], 2: [1, 2,  3, 5], 3: [2, 3, 6],
                   4: [1, 4, 5, 7], 5: [2, 4, 5, 6, 8], 6: [3, 5, 6, 9],
                   7: [4, 7, 8], 8: [0, 5, 7, 8, 9], 9: [6, 8, 9], 0: [0, 8]
                   }
    # Initialize DP table for sequences of length 1
    dp = [[0] * (n + 1) for _ in range(10)]
    for i in range(10):
        dp[i][1] = 1

    # Fill DP table for lengths 2 to n
    for length in range(2, n + 1):
        for digit in range(10):
            dp[digit][length] = sum(dp[prev][length - 1]
                                    for prev in transitions[digit])

    # Sum up the results for sequences of length n
    return sum(dp[digit][n] for digit in range(10))


if __name__ == "__main__":
    print(getCount(2))
    print(getCount(3))
    print(getCount(4))
