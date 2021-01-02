"""
Module to count roots of equations and solve systems
ТУТ 2 ФУНКЦІЇ - 1 ПРОСТО РОЗВ'ЯЗУВАТИ СИСТЕМИ, ІНША - ЗНАХОДИТИ КОРЕНІ БУДЬ-ЯКОГО РІВНЯННЯ
"""

import numpy as np
from sympy import roots
# from workingequat import korni, check_one, step_2

def matritsa(tup):
    """
    function solves systems 
    lst - list of lists of coefficients of each row 
    vec - list of values of each  row one by one
    2x + y + z = 2
    x - y + 0* z = -2
    3x -y + 2z = 2
    answer - [x, y, z] values
    >>> matritsa([[[2.0, 1.0, 1.0], [1.0, -1.0, 0.0], [3.0, -1.0, 2.0]], [2.0, -2.0, 2.0]])
    [-1.  1.  3.]
    """
    matr = np.array(tup[0])
    vector = np.array(tup[1])
    result = np.linalg.solve(matr, vector)
    return result
# print(matritsa([[[1, 1, 0], [-3, -2, -2], [9, 4, 8]], [2, 9, 29]]))

def rivnynnya(equt):
    """
    Function to find al roots (returns a list of them)
    Here: key - root; value - number of its repetitions 
    >>> 'r**2 - 2* r + 1'
    {1: 2}    
    """
    result = roots(equt)
    return result
# print(rivnynnya('r**1 - r*=0'))
