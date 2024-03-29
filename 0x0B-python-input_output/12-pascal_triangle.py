#!/usr/bin/python3
"""definition of a Pascal's Triangle function"""


def pascal_triangle(n):
    """Pascal's Triangle of size n
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for k in range(len(tri) - 1):
            tmp.append(tri[k] + tri[k + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
