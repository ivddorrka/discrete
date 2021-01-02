"""
Working with equations
"""
from countsmth import matritsa, rivnynnya
from readingfiles import userequat, known_roots


def korni(eq):
    """
    Function creates an equation for further work
    >>> 'r = r -4*r +3*r'
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
    >>> 'r**3 - -7*r**2 - -16*r**1 - -12*r**0'
    [('Appear more than 1 time: (root, num of rep-s)', [(-2, 2)]), ('others:', [(-3, 1)])]
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


def step_2(eq):
    """
    For equations, which have some similar roots
    C3 + C1 + 0*C2 = 2
    -3*C3 -2*C1 -2*C2 = 9
    9*C3 + 4*C1 + 8*C2 = 29
    >>> 'r = -7*r -16*r -12*r'
    ([[1, 1, 0], [-3, -2, -2], [9, 4, 8]], [2, 9, 29])
    """
    known_r = known_roots()

    ans = check_one(korni(eq))

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
# print(step_2('r = -7*r -16*r -12*r'))


def find_c(eq):
    """
    Function finds C1 C2 etc according to coef-s from step_2
    >>> 'r = -7*r -16*r -12*r'
    [ 73. -71. -43.]
    """
    inputs_here = step_2(eq)
    return matritsa(inputs_here)
print(find_c('r = 2*r -1*r'))