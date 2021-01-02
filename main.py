"""
Main File, with all functions and work done
"""
import time

from countsmth import rivnynnya, matritsa
from readingfiles import intruction, userequat, known_roots
from workingequat import korni, check_one, step_2, find_c, func1, func2

print(intruction("intro"))
time.sleep(2)

print(2*'\n')

print(intruction("choice_first"))
print('\n')

def asking_output():
    answer = input("Type here: ")
    print('\n')
    if answer not in ['1', '2', '3']:
        time.sleep(1)
        print("Try that again")
        time.sleep(1)
        print('\n')
        return asking_output()
    if answer == '1':
        time.sleep(1)
        print("Приклад: " + '\n' + 'r**1 - r**0' + '\n')
        time.sleep(1)
        ask_2 = input("Введіть рівняння формату як в прикладі: ")
        print("Це <'r**1 - r**0'> те сме, що і <'r**1 - r**0' = 0>")
        print("Не додавайте '=0' в кінці!")
        try: 
            return rivnynnya(ask_2)
        except SyntaxError:
            time.sleep(1)
            print("ВиНиКлА пОмИлКа 0_о" + '\n' + 'Спробуйте ще раз!')
            return asking_output()
    if answer == '2':
        print(intruction("intro"))
        time.sleep(2)
        rivn = userequat()
        known_r = known_roots()
        time.sleep(1)
        ask_3 = input("Введіть кількість перших членів: ")
        time.sleep(1)
        # rivn = userequat()
        try:
            return func2(rivn, int(ask_3), known_r)
        except ValueError:
            time.sleep(1)
            print("ВиНиКлА пОмИлКа 0_о" + '\n' + 'Спробуйте ще раз!')
            return asking_output()
    if answer == '3':
        print(intruction("intro"))
        time.sleep(2)
        rivn = userequat()
        time.sleep(1)
        known_r = known_roots()
        time.sleep(1)
        ask_3 = input("Введіть кількість перших членів: ")
        time.sleep(1)
        try:
            return func1(rivn, int(ask_3), known_r)
        except ValueError:
            time.sleep(1)
            print("ВиНиКлА пОмИлКа 0_о" + '\n' + 'Спробуйте ще раз!')
            return asking_output()
print(asking_output())