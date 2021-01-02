"""
Working with equations
"""
from countsmth import matritsa, rivnynnya
from readingfiles import userequat, known_roots


def korni(eq):
    """
    Function creates an equation for further work
    >>> korni('r = r -4*r +3*r')
    r**3 - r**2 - -4*r**1 - +3*r**0
    """
    members = eq.split() 
    del members[1]
    num_chlenov = len(members) 
    perenos_znaka = ' - '.join(map(str, members)).split()
    new_sh = []
    for i in range(len(perenos_znaka)):
        if i % 2 == 0:
            num_chlenov -= 1
            new = perenos_znaka[i] + '**{}'.format(num_chlenov)
            new_sh.append(new)
    return ' - '.join(map(str, new_sh)) 


def check_one(eq):
    """
    Function checks if there are any repetitions among roots
    >>> check_one(korni('r = -7*r -16*r -12*r'))
    [(-3, 1), (-2, 2)]
    """
    roots_here = rivnynnya(eq)
    keys_here = list(roots_here.keys())
    num_roots  = []
    for i in keys_here:
        val = roots_here.get(i)
        
        res = i, val
        num_roots.append(res)

    return num_roots
# print(check_one(korni('r = -7*r -16*r -12*r')))


def step_2(eq, known_r):
    """
    For equations, which have some similar roots
    C3 + C1 + 0*C2 = 2
    -3*C3 -2*C1 -2*C2 = 9
    9*C3 + 4*C1 + 8*C2 = 29
    >>> step_2('r = -7*r -16*r -12*r', [[0, 2], [1, 9], [2, 29]])
    [[[1, 1, 0], [-3, -2, -2], [9, 4, 8]], [2, 9, 29]]
    """
    # known_r = known_roots()

    root_here = [] # all roots (as many times as they appear)
    vec = [el[1] for el in known_r]
    ind_r = [ele[0] for ele in known_r]
    num_roots = check_one(korni(eq))
    for i in num_roots:
        prom = []
        for j in range((i[1])):
            prom.append(i[0])
        root_here.append(prom)

    emmp = [] # кількість списків = кількості данних коренів, взято в степінь
    for step in ind_r:
        sp = []
        for spisok in root_here:
            new_1 = []
            for elements in spisok:
                elements = elements**step
                new_1.append(elements)
            sp.append(new_1)
        emmp.append(sp)
    
    tabl = []

    for _ in ind_r:
        new_y = []
        for el in emmp:
            new_x = []
            for spiski in el:
                # answer = []
                for elem in range(len(spiski)):
                    res = int(spiski[elem])*(int(ind_r[_])**int(elem))
                    new_x.append(res)
                # new_x.append(answer)
            new_y.append(new_x)
        tabl.append(new_y)
    lst = [] # the list of lists of needed coef-s acco-g to rows
    for pix in range(len(tabl)):
        lst.append(tabl[pix][pix])
    return [lst, vec]
# print(step_2('r = -7*r -16*r -12*r', [[0, 2], [1, 9], [2, 29]]))


def find_c(eq, known_r):
    """
    Function finds C1, C2... etc according to coef-s from step_2
    >>> find_c('r = -7*r -16*r -12*r', [[0, 2], [1, 9], [2, 29]])
    ([73.0, -71.0, -43.0], [(-3, 1), (-2, 2)])
    """
    rrr = check_one(korni(eq))
    inputs_here = step_2(eq, known_r)
    return [round(i, 3) for i in matritsa(inputs_here)], rrr
# print(find_c('r = -7*r -16*r -12*r', [[0, 2], [1, 9], [2, 29]]))


def func1(eq, n, known_r):
    """
    To find n-th members
    >>> func1('r = -3*r +13*r +15*r', 3, [[0, 1], [1, 7], [2, 17]])
    55.0
    """
    inputs = find_c(eq, known_r)
    lst = []
    for i in inputs[1]:
        lst_2 = []
        if i[1] >= 2:
            for j in range(i[1]):
                ress = round((i[0]**n) * inputs[0][0], 2)
                lst_2.append(ress)
                del inputs[0][0]
            lst.append(lst_2)
        else:
            lst_3 = []
            for j in range(i[1]):
                res = round((i[0]**n) * inputs[0][j], 2)
                lst_3.append(res)
                del inputs[0][0]
            lst.append(lst_3)
    result = []
    for _ in lst:
        for element in _:
            ind_el = _.index(element)
            result.append((n**ind_el) * element)
    return round(float(sum(result)), 2)
# print(func1('r = -3*r +13*r +15*r', 3, [[0, 1], [1, 7], [2, 17]]))


def func2(eq, n, known_r):
    """
    >>> func2('r = -3*r +13*r +15*r', 3, [[0, 1], [1, 7], [2, 17]])
    [1.0, 7.0, 17.0, 55.0]
    """
    result = []
    for i in range(n+1):
        res_1 = func1(eq, i, known_r)
        result.append(res_1)
    return result
# print(func2('r = -3*r +13*r +15*r', 3, [[0, 1], [1, 7], [2, 17]]))