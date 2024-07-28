#!/usr/bin/python3


def rowWithMax1s(arr):
    """
    Returns the 0-based index of the first raw
    consisting of the highest count of 1s in the matrix.

    Args:
    - arr: 2D array of only 0s and 1s that will be processed.
    """
    if arr:
        max_count = 0
        max_index = -1
        
        for index in range(len(arr)):
            current_count = sum(arr[index])
            if current_count > max_count:
                max_count = current_count
                max_index = index
        
        # Check if matrix contains no 1s
        if max_count == 0:
            return -1

        return max_index

    return -1


if __name__ == "__main__":
    print(rowWithMax1s([[0, 1, 1, 1],
                        [0, 0, 1, 1],
                        [1, 1, 1, 1],
                        [0, 0, 0, 0]
                        ]))
    print(rowWithMax1s([[0, 0],
                        [1, 1]]))
    print(rowWithMax1s([]))
    print(rowWithMax1s([[0, 1, 1, 1],
                        [0, 0, 1, 1],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1]
                        ]))
    print(rowWithMax1s([[0, 1, 1, 1],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1]
                        ]))
    print(rowWithMax1s([[1],
                        [0],
                        ]))
    print(rowWithMax1s([[0],
                        [0]]))
    print(rowWithMax1s([[1]]))
