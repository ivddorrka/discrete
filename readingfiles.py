"""
To read text from intro and get inputs from user
"""
import time 


def intruction(file):
    """
    to read all text file 
    """
    readingg = open(file, "r")
    return '\n'.join(map(str, list(readingg)))


def userequat():
    """
    to get the start equation
    """
    type_here = input("Введіть ваше рівняння згідно описаних правил ЛАТИНИЦЕЮ: ")
    if 'r' not in type_here.split() or '=' not in type_here.split():
        print("ВиНиКлА пОмИлКа 0_о" + '\n' + 'Спробуйте ще раз!')
        return userequat()
    if len(type_here.split()) < 3:
        print("ВиНиКлА пОмИлКа 0_о" + '\n' + 'Спробуйте ще раз!')
        return userequat()
    else:
        return type_here


def known_roots():
    """
    Function to get all known roots from user
    """
    list_korn = []
    print(2*'\n')
    print("Введіть всі відомі або задані корені послідовно з їхніми індексами: " +'\n')
    time.sleep(1)
    print("Приклад:" + '\n')
    time.sleep(1)
    print("0 2" + '\n' + '1 1')
    time.sleep(1)
    while(True):
        user_input = input("Вводіть тут: ")
        try:
            list_korn.append([int(i) for i in user_input.split()])
        except ValueError:
            print("ВиНиКлА пОмИлКа 0_о" + '\n' + 'Спробуйте ще раз!')
            return known_roots()
        if user_input != '':
            continue
        if user_input == '':
            del list_korn[-1]
            break
    for j in list_korn:
        if len(j) != 2:
            time.sleep(1)
            print("ВиНиКлА пОмИлКа 0_о" + '\n' + 'Спробуйте ще раз!')
            return known_roots()
    return list_korn

# print(known_roots())