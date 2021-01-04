"""
Module to count roots of equations and solve systems
ТУТ 2 ФУНКЦІЇ - 1 ПРОСТО РОЗВ'ЯЗУВАТИ СИСТЕМИ, ІНША - ЗНАХОДИТИ КОРЕНІ БУДЬ-ЯКОГО РІВНЯННЯ
"""
import numpy as np
from sympy import roots


def matritsa(tup):
    """
    >>>

    """
    matr = np.array(tup[0])
    vector = np.array(tup[1])
    result = np.linalg.solve(matr, vector)
    return result
print(matritsa([[[0, 1], [1, 1]], [4, 1]]))

def rivnynnya(equt):
    """
    Function to find all roots (returns a dict of them)
    Here: key - root; value - number of its repetitions 
    >>> 'r**2 - 2* r + 1'
    {1: 2}    
    """
    result = roots(equt)
    return result
# print(rivnynnya('r**3 - r**2 - -4*r**1 - +3*r**0'))


def  cool_out(mn):
    """
    for better output of rivnynnya func
    >>> cool_out(rivnynnya('r**2 - r'))
    x = 1
    x = 0
    """
    korni = list(mn.keys())
    all_known = []
    for i in range(len(korni)):
        res = 'x = {}'.format(korni[i])
        all_known.append(res)
    return '\n'.join(map(str, all_known))
# print(cool_out(rivnynnya('r**2 - r')))