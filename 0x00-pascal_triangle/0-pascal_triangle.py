#!/usr/bin/python3
"""a function to create pascal's triangle"""


def pascal_triangle(n):
    """creation of pascal's triangle"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    if n > 2:
        base = [[1], [1, 1]]
        for i in range(n - 2):
            last = base[-1]
            next = [1]
            for i in range(len(last) - 1):
                next.append(last[i] + last[i + 1])
            next.append(1)
            base.append(next)
    return base
