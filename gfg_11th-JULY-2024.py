#!/usr/bin/python3
from typing import List


def MaxConnection(grid: List[List[int]]) -> int:
    """Returns the maximum number of 1 cells connected"""
    if not grid:
        return 0
    n = len(grid)

    def depth_First(x, y, visited):
        """Do a depth first search"""
        stack = [(x, y)]
        elem = []
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            elem.append((cx, cy))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if (0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1
                   and (nx, ny) not in visited):
                    stack.append((nx, ny))
        return elem

    elems = []
    visited = set()

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and (i, j) not in visited:
                elem = depth_First(i, j, visited)
                elems.append(elem)
    cell_Size = {}
    for elem in elems:
        size = len(elem)
        for cell in elem:
            cell_Size[cell] = size
    connect_Groups = max(cell_Size.values(), default=0)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                near_elem = set()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                        near_elem.add((ni, nj))
                new_group_size = 1
                seen = set()
                for cell in near_elem:
                    comp_size = cell_Size[cell]
                    if comp_size not in seen:
                        new_group_size += comp_size
                        seen.add(comp_size)
                largest = max(connect_Groups, new_group_size)
    return largest


if __name__ == "__main__":
    print(MaxConnection([[0, 1, 0], [0, 1, 0], [0, 1, 0]]))
    print(MaxConnection([[1, 1], [0, 1]]))
    print(MaxConnection([[1, 0, 1], [1, 0, 1], [1, 0, 1]]))
