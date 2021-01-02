"""
To read text from intro and get inputs from user
"""
import time 


def intruction(file):
    """
    to read "intro" file
    """
    readingg = open(file, "r")
    return '\n'.join(map(str, list(readingg)))


def userequat():
    """
    to get the start equation
    """
    type_here = input("Введіть ваше рівняння згідно описаних правил: ")
    if 'r' not in type_here.split() or '=' not in type_here.split():
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
    print("Введіть всі відомі або задані корені так, як показано в прикладі: індекс кореня, його значення " +'\n')
    time.sleep(1)
    print("Приклад:" + '\n')
    time.sleep(1)
    print("0 2")
    time.sleep(1)
    while(True):
        # list_korn = []
        user_input = input("Вводіть тут: ")
        list_korn.append([int(i) for i in user_input.split()])
        if user_input != '':
            continue
        if user_input == '':
            del list_korn[-1]
            break

    # для безкінечного введення відомих коренів

    for i in list_korn:
        if len(i) != 2:
            time.sleep(0.5)
            print("ВиНиКлА пОмИлКа 0_о" + '\n' + 'Спробуйте ще раз!')
            return known_roots()

            #цикл тут перевіряє на наявність і правильність введених данних
    
    return list_korn

# функція повертає список списків, в кожному з яких:
# перший елемент - номер кореня, а другий - значення цього кореня

# print(known_roots())

# ПО СУТІ ЦЕ СТАРТ ПРОЕКТУ