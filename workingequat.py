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

# print(korni('r = -7*r -16*r -12*r'))

def check_one(eq):
    """
    Function checks if there are any repetitions among roots
    >>> 'r**3 - -7*r**2 - -16*r**1 - -12*r**0'
    [('Appear more than 1 time: (root, num of rep-s)', [(-2, 2)]), ('others:', [(-3, 1)])]
    """
    roots_here = rivnynnya(eq)
    keys_here = list(roots_here.keys())
    povtor = []
    not_povtor = []
    for i in keys_here:
        val = roots_here.get(i)
        if val >= 2:
            res = i, val
            povtor.append(res)
        else:
            res_1 = i, val
            not_povtor.append(res_1)
    if len(povtor) >= 1:
        return [("Appear more than 1 time: (root, num of rep-s)", povtor), ("others:", not_povtor)]
    else:
        return ("All roots are different", not_povtor)
# print(check_one(korni('r = 7*r -10*r')))

def step_1(eq):
    """
    Function for case if all roots are different
    Having known roots from user and knowing roots of the equation
    here will be found the coefficients for further calculation
    roots are from check_one
    roots(known) - r(0), r(1) etc - user's inputs
    2 = C1 * 1 + 1 * C2
    1 = C1 * 5 + 2 * C2
    >>> 'r = 7*r -10*r'
    ([[1, 1], [5, 2]], [2, 1])
    """
    known_r = [[0, 2], [1, 1]]
    ans = check_one(korni(eq))
    lst = []
    root_here = [] # here are roots
    for i in ans[1]:
        root_here.append(i[0])
    vec = [_[1] for _ in known_r]
    for i in range(len(known_r)):
        ans = [j**i for j in root_here]
        lst.append(ans)
    return lst, vec
# print(step_1('r = 7*r -10*r'))

def step_2(eq):
    known_r = [[0, 2], [1, 9], [2, 29]]
    # ans = check_one(korni(eq))
    ans = [('Appear more than 1 time: (root, num of rep-s)', [(-2, 2), (3, 3)]), ('others:', [(-3, 1)])]

    root_here = [] # all roots (as many times as they appear)
    
    for i in range(len(ans[0][1])):
        promm = []
        for _ in range((ans[0][1][i][1])):
            promm.append(ans[0][1][i][0])
        root_here.append(promm)

    for j in range(len(ans[1][1][0])):
        for elem in range(ans[1][1][0][j]):
            # root_here.append(ans[1][1][0][0])
            root_here.append(ans[1][1][0][0])

    return root_here
print(step_2('r = -7*r -16*r -12*r'))