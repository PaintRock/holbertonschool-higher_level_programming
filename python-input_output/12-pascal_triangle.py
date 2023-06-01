#!/usr/bin/python3
"""returns a list or lists of integers representing"""


def pascal_triangle(n):
    if n <= 0:
        return []

    result = [[1]]  
    """ Start with the first row"""

    for i in range(1, n):
        row_list = [1]  
        """First element of the row"""

        """ Calculate the elements in between"""
        for j in range(1, i):
            """Sum the adjacent elements from the previous row"""
            element = result[i-1][j-1] + result[i-1][j]
            row_list.append(element)

        row_list.append(1)  
        """Last element of the row"""
        result.append(row_list)  
        """Add the row to the result list"""

    return result
