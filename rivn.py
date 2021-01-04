import numpy as np
from numpy.linalg import matrix_power


def calc_matrices(eq, known_r, n):
    """
    This function calculates remainder after division of n-th element of linear
    recurrent sequence 
    Time complexity of an algorithm is O(log(n)).
    Coefficients of r's must be written in list in order of increase of r.
    :param eq: str
    :param known_r: list
    :param n: int
    :param modulo: int
    :return: int
    >>> calc_matrices('r = 7*r -10*r', [2, 1], 2)
    -101
    >>> calc_matrices('r = 6*r -12*r +8*r', [-5, 4, 88], 3)
    440
    """
    coef_list = get_coefficients(eq)
    matrix = build_matrix(coef_list)
    powered_matrix = matrix_power(matrix, n - (len(known_r) - 1))
    rebuild_matrix = []
    for row in range(len(powered_matrix)):
        prepare = []
        for digit in range(len(powered_matrix[0])):
            prepare.append(powered_matrix[row][digit])
        rebuild_matrix.append(prepare)
    known_r.reverse()
    final_matrix = []
    for elem in range(len(known_r)):
        new_elem = [known_r[elem]]
        final_matrix.append(new_elem)
    result = np.dot(rebuild_matrix, final_matrix)
    return result[0][0]


def build_matrix(coef_list):
    """
    This function builds matrix of linear recurrence with eigenvectors.
    :param coef_list: list
    :return: list
    >>> build_matrix([7, 10])
    [[7, 10], [1, 0]]
    >>> build_matrix([7, 10, -10])
    [[7, 10, -10], [1, 0, 0], [0, 1, 0]]
    """
    final_list = [coef_list]
    for row in range(len(coef_list) - 1):
        ready_row = []
        for num in range(len(coef_list)):
            if row == num:
                ready_row.append(1)
            else:
                ready_row.append(0)
        final_list.append(ready_row)
    return final_list


def get_coefficients(eq):
    """
    To get coef-ts from the equation
    >>> get_coefficients('r = 7*r -10*r')
    [7, -10]
    """
    new_1 = eq.split()
    del new_1[new_1.index('=')]
    del new_1[new_1.index('r')]
    lst = []
    for i in new_1:
        new_2 = list(i)
        del new_2[new_2.index('r')]
        if '*' in new_2: 
            del new_2[new_2.index('*')]
        if '+' in new_2:
            del new_2[new_2.index('+')]
        try:
            res = int(''.join(map(str, new_2)))

            lst.append(res)
        except ValueError:
            lst.append(1)
    return lst
# print(get_coefficients('r = -8r -16*r'))

def modify_roots(lst):
    """
    To modify knoown_roots()
    >>> modify_roots([[0,2], [1, 9], [2, 29]])
    [2, 9, 29]
    """
    res = []
    for i in lst:
        res.append(i[1])
    return res
# print(modify_roots([[0,2], [1, 9], [2, 29]]))
