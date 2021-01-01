"""
Module to count roots of equations and solve systems
ТУТ 2 ФУНКЦІЇ - 1 ПРОСТО РОЗВ'ЯЗУВАТИ СИСТЕМИ, ІНША - ЗНАХОДИТИ КОРЕНІ БУДЬ-ЯКОГО РІВНЯННЯ
"""

import numpy as np
from sympy import roots


def matritsa(lst, vec):
    """
    function solves systems
    >>> matritsa([[2.0, 1.0, 1.0], [1.0, -1.0, 0.0], [3.0, -1.0, 2.0]], [2.0, -2.0, 2.0])
    [-1.  1.  3.]
    """
    matr = np.array(lst)
    vector = np.array(vec)
    result = np.linalg.solve(matr, vector)
    return result
# print(matritsa([[2.0, 1.0, 1.0], [1.0, -1.0, 0.0], [3.0, -1.0, 2.0]], [2.0, -2.0, 2.0]))


def rivnynnya(equt):
    """
    Function to find al roots (returns a list of them)
    >>> 'r**2 + 2*r + 1'
    [-1]
    """
    # result = [r for r in solve(equt) if r.is_real] # щоб знайти лише справжні корені (дискримінант більший = 0)
    result = roots(equt)
    return result
print(rivnynnya('r**2 - 2* r + 1'))

