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
print(intruction("intro"))

time.sleep(1)


def userequat():
    """
    to get the start equation
    # need to fix it to check input
    """
    type_here = input("Type here: ")
    if 'r' not in type_here.split() or '=' not in type_here.split():
        print("Try that again!")
        return userequat()
    else:
        return type_here
# print(userequat())

print(2*'\n')
print("Type now all known/given roots as: root's number it's value" +'\n')
time.sleep(1)
print("EXAMPLE:" + '\n')
time.sleep(1)
print("0 2")


def known_roots():
    """
    Function to get all known roots from user
    """
    list_korn = []
    while(True):
        # list_korn = []
        user_input = input("Type here: ")
        list_korn.append(user_input.split())
        if user_input != '':
            continue
        if user_input == '':
            del list_korn[-1]
            break

    # для безкінечного введення відомих коренів

    for i in list_korn:
        if len(i) != 2:
            time.sleep(0.5)
            print("There's an error, try again")
            return known_roots()

            #цикл тут перевіряє на наявність і правильність введених данних
    
    return list_korn

# функція повертає список списків, в кожному з яких:
# перший елемент - номер кореня, а другий - значення цього кореня

# print(known_roots())

# ПО СУТІ ЦЕ СТАРТ ПРОЕКТУ